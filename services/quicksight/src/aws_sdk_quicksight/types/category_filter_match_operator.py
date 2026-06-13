"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterMatchOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CategoryFilterMatchOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
    "CONTAINS",
    "DOES_NOT_CONTAIN",
    "STARTS_WITH",
    "ENDS_WITH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "DOES_NOT_EQUAL",
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "STARTS_WITH",
        "ENDS_WITH",
    )
)


def serialize_json(value: CategoryFilterMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterMatchOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CategoryFilterMatchOperator value: {data!r}"
        )
    return cast(CategoryFilterMatchOperator, data)
