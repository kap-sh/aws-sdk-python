"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyStorageClass``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyStorageClass: TypeAlias = Literal[
    "ARCHIVE",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecyclePolicyStorageClass:
    return cast(LifecyclePolicyStorageClass, data)
