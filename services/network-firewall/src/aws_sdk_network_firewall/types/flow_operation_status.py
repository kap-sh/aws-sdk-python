"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

FlowOperationStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED_WITH_ERRORS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED_WITH_ERRORS",
    )
)


def serialize_aws_json_1_0(value: FlowOperationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FlowOperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowOperationStatus value: {data!r}")
    return cast(FlowOperationStatus, data)
