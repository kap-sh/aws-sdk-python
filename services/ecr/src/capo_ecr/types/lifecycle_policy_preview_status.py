"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewStatus``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyPreviewStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "EXPIRED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyPreviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecyclePolicyPreviewStatus:
    return cast(LifecyclePolicyPreviewStatus, data)
