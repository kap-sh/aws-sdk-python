"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.lifecycle_policy_preview_result

LifecyclePolicyPreviewResultList: TypeAlias = list[
    "aws_sdk_ecr.types.lifecycle_policy_preview_result.LifecyclePolicyPreviewResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyPreviewResultList) -> list:
    import aws_sdk_ecr.types.lifecycle_policy_preview_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.lifecycle_policy_preview_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LifecyclePolicyPreviewResultList:
    import aws_sdk_ecr.types.lifecycle_policy_preview_result

    out: LifecyclePolicyPreviewResultList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.lifecycle_policy_preview_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
