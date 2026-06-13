"""Generated from Smithy shape ``com.amazonaws.quicksight#QueryExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

QueryExecutionMode: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "MANUAL",
    )
)


def serialize_json(value: QueryExecutionMode) -> str:
    return value


def deserialize_json(data: str) -> QueryExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryExecutionMode value: {data!r}")
    return cast(QueryExecutionMode, data)
