"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAudioStreamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Audio Stream Type"""
M2tsAudioStreamType: TypeAlias = Literal[
    "ATSC",
    "DVB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATSC",
        "DVB",
    )
)


def serialize_json(value: M2tsAudioStreamType) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioStreamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsAudioStreamType value: {data!r}")
    return cast(M2tsAudioStreamType, data)
