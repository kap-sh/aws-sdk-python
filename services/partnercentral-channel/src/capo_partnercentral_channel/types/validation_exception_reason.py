"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "REQUEST_VALIDATION_FAILED",
    "BUSINESS_VALIDATION_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
