"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VisualRole: TypeAlias = Literal[
    "PRIMARY",
    "COMPLIMENTARY",
    "MULTI_INTENT",
    "FALLBACK",
    "FRAGMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "COMPLIMENTARY",
        "MULTI_INTENT",
        "FALLBACK",
        "FRAGMENT",
    )
)


def serialize_json(value: VisualRole) -> str:
    return value


def deserialize_json(data: str) -> VisualRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VisualRole value: {data!r}")
    return cast(VisualRole, data)
