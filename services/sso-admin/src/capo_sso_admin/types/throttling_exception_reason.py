"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ThrottlingExceptionReason``."""

from typing import Literal, TypeAlias, cast

ThrottlingExceptionReason: TypeAlias = Literal["KMS_ThrottlingException",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThrottlingExceptionReason:
    return cast(ThrottlingExceptionReason, data)
