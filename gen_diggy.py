import json
import os
import sys
import zipfile
from pathlib import Path

if (sys.version_info.major, sys.version_info.minor) < (3, 9):
	print('Python 3.9+ is required, current python version: {}'.format(sys.version), file=sys.stderr)
	sys.exit(1)


MC_CONFIG = {
	'1.15': {
		'diggy_function_path': 'data/diggy/functions',
		'tag_function_path': 'data/minecraft/tags/functions',
		'pack_format': 4,
		'netherite': False
	},
	'1.16': {
		'diggy_function_path': 'data/diggy/functions',
		'tag_function_path': 'data/minecraft/tags/functions',
		'pack_format': 5,
		'netherite': True
	},
	'1.21': {
		'diggy_function_path': 'data/diggy/function',
		'tag_function_path': 'data/minecraft/tags/function',
		'pack_format': 48,
		'netherite': True
	},
}
LANGS = {
	'en': {
		'title_pickaxe': 'Diggy (pickaxe)',
		'title_axe': 'Diggy (axe)',
		'title_shovel': 'Diggy (shovel)',
		'title_hoe': 'Diggy (hoe)',
		'title_shears': 'Diggy (shears)',
		'title_all': 'Diggy (sum)',
	},
	'zh': {
		'title_pickaxe': '挖掘榜(镐)',
		'title_axe': '挖掘榜(斧)',
		'title_shovel': '挖掘榜(锹)',
		'title_hoe': '挖掘榜(锄)',
		'title_shears': '挖掘榜(剪刀)',
		'title_all': '挖掘榜(总)',
	},
}

VERSION = '1.1'
DATAPACK_NAME = 'DiggyScoreboard'

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / 'output'
TEMPLATE_DIR = HERE / 'template'
DIGGY_FUNCTIONS_DIR = TEMPLATE_DIR / 'diggy_functions'
PACK_META_FILE = TEMPLATE_DIR / 'pack.mcmeta'
TICK_JSON_FILE = TEMPLATE_DIR / 'tick.json'


def read_file(path: Path) -> str:
	with open(path, 'r', encoding='utf8') as f:
		return f.read()


def gen_one(mc: str, lang: str, output_path: Path):
	config = MC_CONFIG[mc]

	with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
		def write(path_in_datapack: Path or str, str_to_write: str):
			zipf.writestr(Path(path_in_datapack).as_posix(), str_to_write)

		# pack.mcmeta
		s = read_file(PACK_META_FILE)
		s = s.replace('{{pack_format}}', str(config['pack_format']))
		write(PACK_META_FILE.name, s)

		# tick.json
		s = read_file(TICK_JSON_FILE)
		write(Path(config['tag_function_path']) / TICK_JSON_FILE.name, s)

		# functions
		for name in os.listdir(DIGGY_FUNCTIONS_DIR):
			path = DIGGY_FUNCTIONS_DIR / name
			if not (name.endswith('.mcfunction') and path.is_file()):
				continue

			lines = read_file(path).splitlines(keepends=False)
			new_lines: list[str] = []

			for line in lines:
				nrs = '//NETHERITE//'
				if line.endswith(nrs):
					line = line[:-len(nrs)].rstrip(' ')
					if config['netherite'] is False:
						continue
				for key, value in LANGS[lang].items():
					line = line.replace('{{' + key + '}}', json.dumps(str(value), ensure_ascii=False))
				new_lines.append(line)

			write(Path(config['diggy_function_path']) / name, '\n'.join(new_lines))


def main():
	OUTPUT_DIR.mkdir(exist_ok=True)

	for mc in MC_CONFIG:
		for lang in LANGS:
			file_name = f'{DATAPACK_NAME}_v{VERSION}_mc{mc}_{lang}.zip'
			print('Generating mc={} lang={} file={}'.format(mc, lang, file_name))
			gen_one(mc, lang, OUTPUT_DIR / file_name)


if __name__ == '__main__':
	main()
