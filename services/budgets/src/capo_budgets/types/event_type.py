"""Generated from Smithy shape ``com.amazonaws.budgets#EventType``."""

from typing import Literal, TypeAlias, cast

EventType: TypeAlias = Literal[
    "SYSTEM",
    "CREATE_ACTION",
    "DELETE_ACTION",
    "UPDATE_ACTION",
    "EXECUTE_ACTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventType:
    return cast(EventType, data)
