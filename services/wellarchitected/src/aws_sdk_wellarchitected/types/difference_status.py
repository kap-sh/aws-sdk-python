"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DifferenceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

DifferenceStatus: TypeAlias = Literal[
    "UPDATED",
    "NEW",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATED",
        "NEW",
        "DELETED",
    )
)


def serialize_json(value: DifferenceStatus) -> str:
    return value


def deserialize_json(data: str) -> DifferenceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DifferenceStatus value: {data!r}")
    return cast(DifferenceStatus, data)
