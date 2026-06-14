"""Generated from Smithy shape ``com.amazonaws.datazone#SortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SortKey: TypeAlias = Literal[
    "CREATED_AT",
    "UPDATED_AT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED_AT",
        "UPDATED_AT",
    )
)


def serialize_json(value: SortKey) -> str:
    return value


def deserialize_json(data: str) -> SortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortKey value: {data!r}")
    return cast(SortKey, data)
