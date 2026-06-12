"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DifferenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

DifferenceType: TypeAlias = Literal[
    "NotEqual",
    "Added",
    "Removed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotEqual",
        "Added",
        "Removed",
    )
)


def serialize_json(value: DifferenceType) -> str:
    return value


def deserialize_json(data: str) -> DifferenceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DifferenceType value: {data!r}")
    return cast(DifferenceType, data)
