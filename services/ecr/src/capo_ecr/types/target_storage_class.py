"""Generated from Smithy shape ``com.amazonaws.ecr#TargetStorageClass``."""

from typing import Literal, TypeAlias, cast

TargetStorageClass: TypeAlias = Literal[
    "STANDARD",
    "ARCHIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetStorageClass:
    return cast(TargetStorageClass, data)
