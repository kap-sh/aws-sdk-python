"""Generated from Smithy shape ``com.amazonaws.quicksight#PropertyRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PropertyRole: TypeAlias = Literal[
    "PRIMARY",
    "ID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "ID",
    )
)


def serialize_json(value: PropertyRole) -> str:
    return value


def deserialize_json(data: str) -> PropertyRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyRole value: {data!r}")
    return cast(PropertyRole, data)
