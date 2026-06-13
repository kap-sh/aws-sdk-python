"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringComparisonFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetStringComparisonFilterOperator: TypeAlias = Literal[
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


def serialize_json(value: DataSetStringComparisonFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetStringComparisonFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSetStringComparisonFilterOperator value: {data!r}"
        )
    return cast(DataSetStringComparisonFilterOperator, data)
