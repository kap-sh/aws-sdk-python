"""Generated from Smithy shape ``com.amazonaws.eventbridge#EventSourceState``."""

from typing import Literal, TypeAlias, cast

EventSourceState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSourceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSourceState:
    return cast(EventSourceState, data)
