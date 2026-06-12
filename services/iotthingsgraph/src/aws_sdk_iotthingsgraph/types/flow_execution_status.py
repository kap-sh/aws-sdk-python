"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

FlowExecutionStatus: TypeAlias = Literal[
    "RUNNING",
    "ABORTED",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "ABORTED",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: FlowExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionStatus value: {data!r}")
    return cast(FlowExecutionStatus, data)
