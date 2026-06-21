"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEncryptionMode``."""

from typing import Literal, TypeAlias, cast

DataQualityEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEncryptionMode:
    return cast(DataQualityEncryptionMode, data)
