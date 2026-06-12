"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "PENDING_CONCURRENCY",
    "PENDING_DEVICE",
    "PROCESSING",
    "SCHEDULING",
    "PREPARING",
    "RUNNING",
    "COMPLETED",
    "STOPPING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "PENDING_CONCURRENCY",
        "PENDING_DEVICE",
        "PROCESSING",
        "SCHEDULING",
        "PREPARING",
        "RUNNING",
        "COMPLETED",
        "STOPPING",
    )
)


def serialize_aws_json_1_1(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
