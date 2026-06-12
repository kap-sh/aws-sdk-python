"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264CodecLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify an H.264 level that is consistent with your output video settings. If you aren't sure what level to specify, choose Auto."""
H264CodecLevel: TypeAlias = Literal[
    "AUTO",
    "LEVEL_1",
    "LEVEL_1_1",
    "LEVEL_1_2",
    "LEVEL_1_3",
    "LEVEL_2",
    "LEVEL_2_1",
    "LEVEL_2_2",
    "LEVEL_3",
    "LEVEL_3_1",
    "LEVEL_3_2",
    "LEVEL_4",
    "LEVEL_4_1",
    "LEVEL_4_2",
    "LEVEL_5",
    "LEVEL_5_1",
    "LEVEL_5_2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "LEVEL_1",
        "LEVEL_1_1",
        "LEVEL_1_2",
        "LEVEL_1_3",
        "LEVEL_2",
        "LEVEL_2_1",
        "LEVEL_2_2",
        "LEVEL_3",
        "LEVEL_3_1",
        "LEVEL_3_2",
        "LEVEL_4",
        "LEVEL_4_1",
        "LEVEL_4_2",
        "LEVEL_5",
        "LEVEL_5_1",
        "LEVEL_5_2",
    )
)


def serialize_json(value: H264CodecLevel) -> str:
    return value


def deserialize_json(data: str) -> H264CodecLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264CodecLevel value: {data!r}")
    return cast(H264CodecLevel, data)
