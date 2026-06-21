"""Generated from Smithy shape ``com.amazonaws.identitystore#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "KMS_INVALID_ARN",
    "KMS_INVALID_KEY_USAGE",
    "KMS_INVALID_STATE",
    "KMS_DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
