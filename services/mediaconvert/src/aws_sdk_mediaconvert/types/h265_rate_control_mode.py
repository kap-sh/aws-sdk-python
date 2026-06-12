"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR)."""
H265RateControlMode: TypeAlias = Literal[
    "VBR",
    "CBR",
    "QVBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VBR",
        "CBR",
        "QVBR",
    )
)


def serialize_json(value: H265RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> H265RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265RateControlMode value: {data!r}")
    return cast(H265RateControlMode, data)
