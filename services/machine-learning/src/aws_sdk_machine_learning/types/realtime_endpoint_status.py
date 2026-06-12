"""Generated from Smithy shape ``com.amazonaws.machinelearning#RealtimeEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

RealtimeEndpointStatus: TypeAlias = Literal[
    "NONE",
    "READY",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "READY",
        "UPDATING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: RealtimeEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RealtimeEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RealtimeEndpointStatus value: {data!r}")
    return cast(RealtimeEndpointStatus, data)
