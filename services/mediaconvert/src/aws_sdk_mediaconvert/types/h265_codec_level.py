"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265CodecLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""H.265 Level."""
H265CodecLevel: TypeAlias = Literal[
    "AUTO",
    "LEVEL_1",
    "LEVEL_2",
    "LEVEL_2_1",
    "LEVEL_3",
    "LEVEL_3_1",
    "LEVEL_4",
    "LEVEL_4_1",
    "LEVEL_5",
    "LEVEL_5_1",
    "LEVEL_5_2",
    "LEVEL_6",
    "LEVEL_6_1",
    "LEVEL_6_2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "LEVEL_1",
        "LEVEL_2",
        "LEVEL_2_1",
        "LEVEL_3",
        "LEVEL_3_1",
        "LEVEL_4",
        "LEVEL_4_1",
        "LEVEL_5",
        "LEVEL_5_1",
        "LEVEL_5_2",
        "LEVEL_6",
        "LEVEL_6_1",
        "LEVEL_6_2",
    )
)


def serialize_json(value: H265CodecLevel) -> str:
    return value


def deserialize_json(data: str) -> H265CodecLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265CodecLevel value: {data!r}")
    return cast(H265CodecLevel, data)
