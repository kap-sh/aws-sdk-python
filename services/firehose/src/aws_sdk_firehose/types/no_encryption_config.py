"""Generated from Smithy shape ``com.amazonaws.firehose#NoEncryptionConfig``."""

from typing import Literal, TypeAlias, cast

NoEncryptionConfig: TypeAlias = Literal["NoEncryption",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoEncryptionConfig) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NoEncryptionConfig:
    return cast(NoEncryptionConfig, data)
