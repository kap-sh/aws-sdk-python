"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildMessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AutomatedReasoningPolicyBuildMessageType: TypeAlias = Literal[
    "INFO",
    "WARNING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFO",
        "WARNING",
        "ERROR",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildMessageType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildMessageType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildMessageType value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildMessageType, data)
