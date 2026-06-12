"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ComponentStatus: TypeAlias = Literal[
    "DEPRECATED",
    "DISABLED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPRECATED",
        "DISABLED",
        "ACTIVE",
    )
)


def serialize_json(value: ComponentStatus) -> str:
    return value


def deserialize_json(data: str) -> ComponentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentStatus value: {data!r}")
    return cast(ComponentStatus, data)
