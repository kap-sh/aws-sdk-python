"""Generated from Smithy shape ``com.amazonaws.deadline#LogicalOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

LogicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_json(value: LogicalOperator) -> str:
    return value


def deserialize_json(data: str) -> LogicalOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogicalOperator value: {data!r}")
    return cast(LogicalOperator, data)
