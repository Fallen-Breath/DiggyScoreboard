Diggy Scoreboard
-------------------

Lite datapack for tool uses related scoreboard, diggy diggy~

Use `/function diggy:install` to install, `/function diggy:uninstall` to uninstall

There are 6 scoreboards are for displaying:

- `dig-pickaxe`: The total uses of all types of pickaxes
- `dig-axe`: The total uses of all types of axes
- `dig-shovel`: The total uses of all types of shovels
- `dig-hoe`: The total uses of all types of hoes
- `dig-shears`: The total uses of shears
- `dig-all`: Sum of every uses above

Example usage: `/scoreboard objectives setdisplay sidebar dig-all`

Scoreboard display names are store in `data/diggy/functions/install.mcfunction`, change them if you want custom names before install

You can use command like `/execute as @a run scoreboard players operation @s dig-all += @s my_old_pickuse` to update diggy scoreboards from existing scoreboard

-------------------

挖掘计分板
-------------------

一个用于显示工具使用次数计分板的轻量数据包，挖挖挖~

用`/function diggy:install` 来安装，`/function diggy:uninstall` 来卸载

共有 6 个用于展示的计分板

- `dig-pickaxe`：所有镐的总使用次数
- `dig-axe`：所有斧的总使用次数
- `dig-shovel`：所有锹的总使用次数
- `dig-hoe`：所有锄的总使用次数
- `dig-shears`：剪刀的使用次数
- `dig-all`：以上所有的总使用次数

用法举例： `/scoreboard objectives setdisplay sidebar dig-all`

计分板的名字储存于 `data/diggy/functions/install.mcfunction`，如果你想要自定义名称的话请在安装前修改

你可以用形如 `/execute as @a run scoreboard players operation @s dig-all += @s my_old_pickuse` 的指令来将已有的计分板导入数据至该挖掘计分板