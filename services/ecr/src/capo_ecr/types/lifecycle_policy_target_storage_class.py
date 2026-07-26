"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyTargetStorageClass``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyTargetStorageClass: TypeAlias = Literal["ARCHIVE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyTargetStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecyclePolicyTargetStorageClass:
    return cast(LifecyclePolicyTargetStorageClass, data)
