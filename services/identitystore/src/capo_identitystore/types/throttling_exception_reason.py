"""Generated from Smithy shape ``com.amazonaws.identitystore#ThrottlingExceptionReason``."""

from typing import Literal, TypeAlias, cast

ThrottlingExceptionReason: TypeAlias = Literal["KMS_THROTTLING",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThrottlingExceptionReason:
    return cast(ThrottlingExceptionReason, data)
