"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "CannotParse",
    "FieldValidationFailed",
    "IdempotentParameterMismatchException",
    "EventInOtherSession",
    "ResourceConflict",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CannotParse",
        "FieldValidationFailed",
        "IdempotentParameterMismatchException",
        "EventInOtherSession",
        "ResourceConflict",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
