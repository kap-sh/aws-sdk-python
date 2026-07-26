"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "INVALID_CA_SUBJECT",
    "INVALID_PERMISSION",
    "INVALID_STATE",
    "MISMATCHED_CONNECTOR",
    "MISMATCHED_VPC",
    "NO_CLIENT_TOKEN",
    "UNKNOWN_OPERATION",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
