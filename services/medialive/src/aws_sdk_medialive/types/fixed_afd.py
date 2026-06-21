"""Generated from Smithy shape ``com.amazonaws.medialive#FixedAfd``."""

from typing import Literal, TypeAlias, cast

"""Fixed Afd"""
FixedAfd: TypeAlias = Literal[
    "AFD_0000",
    "AFD_0010",
    "AFD_0011",
    "AFD_0100",
    "AFD_1000",
    "AFD_1001",
    "AFD_1010",
    "AFD_1011",
    "AFD_1101",
    "AFD_1110",
    "AFD_1111",
]


# --- restJson1 ser/de ---
def serialize_json(value: FixedAfd) -> str:
    return value


def deserialize_json(data: str) -> FixedAfd:
    return cast(FixedAfd, data)
