"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EventStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

EventStatus: TypeAlias = Literal[
    "Ready",
    "InProgress",
    "Complete",
    "Failed",
    "Cancelled",
    "RollbackReady",
    "RollbackInProgress",
    "RollbackComplete",
    "RollbackFailed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ready",
        "InProgress",
        "Complete",
        "Failed",
        "Cancelled",
        "RollbackReady",
        "RollbackInProgress",
        "RollbackComplete",
        "RollbackFailed",
    )
)


def serialize_aws_json_1_0(value: EventStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventStatus value: {data!r}")
    return cast(EventStatus, data)
