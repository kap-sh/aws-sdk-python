"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplicationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

ReplicationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ReplicationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationState value: {data!r}")
    return cast(ReplicationState, data)
