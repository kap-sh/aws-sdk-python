"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsRateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate."""
M2tsRateMode: TypeAlias = Literal[
    "VBR",
    "CBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VBR",
        "CBR",
    )
)


def serialize_json(value: M2tsRateMode) -> str:
    return value


def deserialize_json(data: str) -> M2tsRateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsRateMode value: {data!r}")
    return cast(M2tsRateMode, data)
