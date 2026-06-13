"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringListFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetStringListFilterOperator: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: DataSetStringListFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> DataSetStringListFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataSetStringListFilterOperator value: {data!r}"
        )
    return cast(DataSetStringListFilterOperator, data)
