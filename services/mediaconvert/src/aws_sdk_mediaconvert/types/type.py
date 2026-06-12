"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

Type: TypeAlias = Literal[
    "SYSTEM",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM",
        "CUSTOM",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
