"""Generated from Smithy shape ``com.amazonaws.sagemaker#StorageType``."""

from typing import Literal, TypeAlias, cast

StorageType: TypeAlias = Literal[
    "Standard",
    "InMemory",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageType:
    return cast(StorageType, data)
