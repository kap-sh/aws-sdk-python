"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedStorageType``."""

from typing import Literal, TypeAlias, cast

ManagedStorageType: TypeAlias = Literal["Restricted",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedStorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedStorageType:
    return cast(ManagedStorageType, data)
