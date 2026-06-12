"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265UnregisteredSeiTimecode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Inserts timecode for each frame as 4 bytes of an unregistered SEI message."""
H265UnregisteredSeiTimecode: TypeAlias = Literal[
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


def serialize_json(value: H265UnregisteredSeiTimecode) -> str:
    return value


def deserialize_json(data: str) -> H265UnregisteredSeiTimecode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265UnregisteredSeiTimecode value: {data!r}"
        )
    return cast(H265UnregisteredSeiTimecode, data)
