"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericComparisonFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetNumericComparisonFilterOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "DOES_NOT_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUALS_TO",
        "LESS_THAN",
        "LESS_THAN_OR_EQUALS_TO",
    )
)


def serialize_json(value: DataSetNumericComparisonFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetNumericComparisonFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSetNumericComparisonFilterOperator value: {data!r}"
        )
    return cast(DataSetNumericComparisonFilterOperator, data)
