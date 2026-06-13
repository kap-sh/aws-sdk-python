"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericEqualityMatchOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NumericEqualityMatchOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "DOES_NOT_EQUAL",
    )
)


def serialize_json(value: NumericEqualityMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> NumericEqualityMatchOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NumericEqualityMatchOperator value: {data!r}"
        )
    return cast(NumericEqualityMatchOperator, data)
