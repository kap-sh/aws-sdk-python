"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsEbifControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Ebif Control"""
M2tsEbifControl: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PASSTHROUGH",
    )
)


def serialize_json(value: M2tsEbifControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbifControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsEbifControl value: {data!r}")
    return cast(M2tsEbifControl, data)
