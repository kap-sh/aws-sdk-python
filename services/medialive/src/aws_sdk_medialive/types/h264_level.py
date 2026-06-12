"""Generated from Smithy shape ``com.amazonaws.medialive#H264Level``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: H264Level) -> str:
    return value


def deserialize_json(data: str) -> H264Level:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264Level value: {data!r}")
    return cast(H264Level, data)
