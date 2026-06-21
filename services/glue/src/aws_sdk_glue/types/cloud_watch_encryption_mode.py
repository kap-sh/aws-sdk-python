"""Generated from Smithy shape ``com.amazonaws.glue#CloudWatchEncryptionMode``."""

from typing import Literal, TypeAlias, cast

CloudWatchEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudWatchEncryptionMode:
    return cast(CloudWatchEncryptionMode, data)
