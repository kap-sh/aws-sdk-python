"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildDocumentContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningPolicyBuildDocumentContentType: TypeAlias = Literal[
    "pdf",
    "txt",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pdf",
        "txt",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildDocumentContentType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildDocumentContentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildDocumentContentType value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildDocumentContentType, data)
