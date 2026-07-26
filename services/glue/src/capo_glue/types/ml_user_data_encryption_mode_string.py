"""Generated from Smithy shape ``com.amazonaws.glue#MLUserDataEncryptionModeString``."""

from typing import Literal, TypeAlias, cast

MLUserDataEncryptionModeString: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MLUserDataEncryptionModeString) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MLUserDataEncryptionModeString:
    return cast(MLUserDataEncryptionModeString, data)
