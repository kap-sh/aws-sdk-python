"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
