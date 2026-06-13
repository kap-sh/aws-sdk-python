"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningPolicyBuildWorkflowStatus: TypeAlias = Literal[
    "SCHEDULED",
    "CANCEL_REQUESTED",
    "PREPROCESSING",
    "BUILDING",
    "TESTING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "CANCEL_REQUESTED",
        "PREPROCESSING",
        "BUILDING",
        "TESTING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildWorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildWorkflowStatus value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildWorkflowStatus, data)
