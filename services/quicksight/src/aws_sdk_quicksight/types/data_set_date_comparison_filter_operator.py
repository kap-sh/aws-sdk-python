"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateComparisonFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetDateComparisonFilterOperator: TypeAlias = Literal[
    "BEFORE",
    "BEFORE_OR_EQUALS_TO",
    "AFTER",
    "AFTER_OR_EQUALS_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE",
        "BEFORE_OR_EQUALS_TO",
        "AFTER",
        "AFTER_OR_EQUALS_TO",
    )
)


def serialize_json(value: DataSetDateComparisonFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetDateComparisonFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSetDateComparisonFilterOperator value: {data!r}"
        )
    return cast(DataSetDateComparisonFilterOperator, data)
