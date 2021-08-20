# 算法来自 https://www.bilibili.com/video/av674891654

from typing import Tuple

from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, old):
    server.register_command(
        Literal("!!diamond").then(
            Integer("seed").then(
                Integer("x").then(
                    Integer("z").runs(lambda src, ctx: callback(src, ctx))
                )
            )
        )
    )


def callback(src: CommandSource, ctx: dict):
    print(ctx)
    pos = calculator(ctx["seed"], ctx["x"], ctx["z"])
    src.reply("X: {x}, Z: {z}".format(x=pos[0], z=pos[1]))


def calculator(seed: int, x: int, z: int) -> Tuple[int, int]:
    mul = 25214903917
    mask = (1 << 48) - 1
    t = seed ^ mul & mask
    t = (t * mul + 11) & mask
    t1 = t >> 16 << 32
    t = (t * mul + 11) & mask
    t2 = t << 16 >> 32
    t = (t * mul + 11) & mask
    t3 = t >> 16 << 32
    t = (t * mul + 11) & mask
    t4 = t << 16 >> 32
    i = (t1 + t2) | 1
    j = (t3 + t4) | 1
    t = (16 * x * i + 16 * z * j) ^ seed + 60009
    t = t ^ mul & mask
    t = (t * mul + 11) & mask
    rel_x = t >> 44
    t = (t * mul + 11) & mask
    rel_z = t >> 44
    return (rel_x + 16 * x), (rel_z + 16 * z)
