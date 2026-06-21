"""Generated from Smithy shape ``com.amazonaws.identitystore#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

ResourceNotFoundExceptionReason: TypeAlias = Literal["KMS_KEY_NOT_FOUND",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceNotFoundExceptionReason:
    return cast(ResourceNotFoundExceptionReason, data)
