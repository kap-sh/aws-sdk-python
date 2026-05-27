"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.fargate_profile_selector

FargateProfileSelectors: TypeAlias = list[
    "aws_sdk_eks.types.fargate_profile_selector.FargateProfileSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileSelectors) -> list:
    import aws_sdk_eks.types.fargate_profile_selector

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.fargate_profile_selector.serialize_json(item))
    return out


def deserialize_json(data: list) -> FargateProfileSelectors:
    import aws_sdk_eks.types.fargate_profile_selector

    out: FargateProfileSelectors = []
    for item in data:
        out.append(aws_sdk_eks.types.fargate_profile_selector.deserialize_json(item))
    return out
