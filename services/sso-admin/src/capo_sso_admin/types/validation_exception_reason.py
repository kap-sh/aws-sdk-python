"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "KMS_InvalidKeyUsageException",
    "KMS_InvalidStateException",
    "KMS_DisabledException",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
