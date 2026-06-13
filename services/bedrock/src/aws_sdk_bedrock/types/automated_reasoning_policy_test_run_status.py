"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningPolicyTestRunStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "SCHEDULED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "SCHEDULED",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyTestRunStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyTestRunStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyTestRunStatus value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyTestRunStatus, data)
