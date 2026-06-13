"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestRunResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningPolicyTestRunResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyTestRunResult) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyTestRunResult:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyTestRunResult value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyTestRunResult, data)
