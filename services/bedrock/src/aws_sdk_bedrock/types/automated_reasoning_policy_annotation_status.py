"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningPolicyAnnotationStatus: TypeAlias = Literal[
    "APPLIED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLIED",
        "FAILED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyAnnotationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyAnnotationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyAnnotationStatus value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyAnnotationStatus, data)
