"""Generated from Smithy shape ``com.amazonaws.budgets#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

EventType: TypeAlias = Literal[
    "SYSTEM",
    "CREATE_ACTION",
    "DELETE_ACTION",
    "UPDATE_ACTION",
    "EXECUTE_ACTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM",
        "CREATE_ACTION",
        "DELETE_ACTION",
        "UPDATE_ACTION",
        "EXECUTE_ACTION",
    )
)


def serialize_aws_json_1_1(value: EventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
