"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CategoryFilterFunction: TypeAlias = Literal[
    "EXACT",
    "CONTAINS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXACT",
        "CONTAINS",
    )
)


def serialize_json(value: CategoryFilterFunction) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterFunction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CategoryFilterFunction value: {data!r}")
    return cast(CategoryFilterFunction, data)
