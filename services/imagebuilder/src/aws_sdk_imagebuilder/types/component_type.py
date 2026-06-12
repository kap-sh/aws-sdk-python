"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ComponentType: TypeAlias = Literal[
    "BUILD",
    "TEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD",
        "TEST",
    )
)


def serialize_json(value: ComponentType) -> str:
    return value


def deserialize_json(data: str) -> ComponentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentType value: {data!r}")
    return cast(ComponentType, data)
