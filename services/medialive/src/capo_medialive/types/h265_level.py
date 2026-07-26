"""Generated from Smithy shape ``com.amazonaws.medialive#H265Level``."""

from typing import Literal, TypeAlias, cast

"""H265 Level"""
H265Level: TypeAlias = Literal[
    "H265_LEVEL_1",
    "H265_LEVEL_2",
    "H265_LEVEL_2_1",
    "H265_LEVEL_3",
    "H265_LEVEL_3_1",
    "H265_LEVEL_4",
    "H265_LEVEL_4_1",
    "H265_LEVEL_5",
    "H265_LEVEL_5_1",
    "H265_LEVEL_5_2",
    "H265_LEVEL_6",
    "H265_LEVEL_6_1",
    "H265_LEVEL_6_2",
    "H265_LEVEL_AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265Level) -> str:
    return value


def deserialize_json(data: str) -> H265Level:
    return cast(H265Level, data)
