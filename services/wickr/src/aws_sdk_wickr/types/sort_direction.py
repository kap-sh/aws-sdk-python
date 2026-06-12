"""Generated from Smithy shape ``com.amazonaws.wickr#SortDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wickr.errors import DeserializationError

SortDirection: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: SortDirection) -> str:
    return value


def deserialize_json(data: str) -> SortDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortDirection value: {data!r}")
    return cast(SortDirection, data)
