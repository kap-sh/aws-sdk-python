"""Generated from Smithy shape ``com.amazonaws.quicksight#PersonalizationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PersonalizationMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: PersonalizationMode) -> str:
    return value


def deserialize_json(data: str) -> PersonalizationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PersonalizationMode value: {data!r}")
    return cast(PersonalizationMode, data)
