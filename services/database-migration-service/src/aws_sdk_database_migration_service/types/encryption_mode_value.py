"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EncryptionModeValue``."""

from typing import Literal, TypeAlias, cast

EncryptionModeValue: TypeAlias = Literal[
    "sse-s3",
    "sse-kms",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionModeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionModeValue:
    return cast(EncryptionModeValue, data)
