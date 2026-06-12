"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264RepeatPps``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Places a PPS header on each encoded picture, even if repeated."""
H264RepeatPps: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H264RepeatPps) -> str:
    return value


def deserialize_json(data: str) -> H264RepeatPps:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264RepeatPps value: {data!r}")
    return cast(H264RepeatPps, data)
