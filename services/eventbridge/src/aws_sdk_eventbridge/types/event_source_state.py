"""Generated from Smithy shape ``com.amazonaws.eventbridge#EventSourceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

EventSourceState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: EventSourceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSourceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceState value: {data!r}")
    return cast(EventSourceState, data)
