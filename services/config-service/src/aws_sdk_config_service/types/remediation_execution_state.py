"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RemediationExecutionState: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: RemediationExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RemediationExecutionState value: {data!r}")
    return cast(RemediationExecutionState, data)
