"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionStepState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RemediationExecutionStepState: TypeAlias = Literal[
    "SUCCEEDED",
    "PENDING",
    "FAILED",
    "IN_PROGRESS",
    "EXITED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "PENDING",
        "FAILED",
        "IN_PROGRESS",
        "EXITED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: RemediationExecutionStepState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationExecutionStepState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RemediationExecutionStepState value: {data!r}"
        )
    return cast(RemediationExecutionStepState, data)
