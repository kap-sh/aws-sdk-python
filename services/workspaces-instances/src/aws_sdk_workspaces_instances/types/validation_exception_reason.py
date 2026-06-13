"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "UNKNOWN_OPERATION",
    "UNSUPPORTED_OPERATION",
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "DEPENDENCY_FAILURE",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN_OPERATION",
        "UNSUPPORTED_OPERATION",
        "CANNOT_PARSE",
        "FIELD_VALIDATION_FAILED",
        "DEPENDENCY_FAILURE",
        "OTHER",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
