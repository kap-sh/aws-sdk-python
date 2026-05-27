"""Generated from Smithy shape ``com.amazonaws.eks#AddonCompatibilityDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_compatibility_detail

AddonCompatibilityDetails: TypeAlias = list[
    "aws_sdk_eks.types.addon_compatibility_detail.AddonCompatibilityDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonCompatibilityDetails) -> list:
    import aws_sdk_eks.types.addon_compatibility_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.addon_compatibility_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> AddonCompatibilityDetails:
    import aws_sdk_eks.types.addon_compatibility_detail

    out: AddonCompatibilityDetails = []
    for item in data:
        out.append(aws_sdk_eks.types.addon_compatibility_detail.deserialize_json(item))
    return out
