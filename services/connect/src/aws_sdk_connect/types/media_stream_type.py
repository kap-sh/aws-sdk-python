"""Generated from Smithy shape ``com.amazonaws.connect#MediaStreamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

MediaStreamType: TypeAlias = Literal[
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIO",
        "VIDEO",
    )
)


def serialize_json(value: MediaStreamType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaStreamType value: {data!r}")
    return cast(MediaStreamType, data)
