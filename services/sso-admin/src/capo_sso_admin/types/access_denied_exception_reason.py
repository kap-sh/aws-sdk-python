"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionReason: TypeAlias = Literal["KMS_AccessDeniedException",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)
