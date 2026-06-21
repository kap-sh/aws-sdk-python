"""Generated from Smithy shape ``com.amazonaws.glue#JobBookmarksEncryptionMode``."""

from typing import Literal, TypeAlias, cast

JobBookmarksEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "CSE-KMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobBookmarksEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobBookmarksEncryptionMode:
    return cast(JobBookmarksEncryptionMode, data)
