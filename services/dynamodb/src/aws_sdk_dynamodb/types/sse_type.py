"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSEType``."""

from typing import Literal, TypeAlias, cast

SSEType: TypeAlias = Literal[
    "AES256",
    "KMS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SSEType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SSEType:
    return cast(SSEType, data)
