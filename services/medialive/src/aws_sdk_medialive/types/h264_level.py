"""Generated from Smithy shape ``com.amazonaws.medialive#H264Level``."""

from typing import Literal, TypeAlias, cast

"""H264 Level"""
H264Level: TypeAlias = Literal[
    "H264_LEVEL_1",
    "H264_LEVEL_1_1",
    "H264_LEVEL_1_2",
    "H264_LEVEL_1_3",
    "H264_LEVEL_2",
    "H264_LEVEL_2_1",
    "H264_LEVEL_2_2",
    "H264_LEVEL_3",
    "H264_LEVEL_3_1",
    "H264_LEVEL_3_2",
    "H264_LEVEL_4",
    "H264_LEVEL_4_1",
    "H264_LEVEL_4_2",
    "H264_LEVEL_5",
    "H264_LEVEL_5_1",
    "H264_LEVEL_5_2",
    "H264_LEVEL_AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264Level) -> str:
    return value


def deserialize_json(data: str) -> H264Level:
    return cast(H264Level, data)
