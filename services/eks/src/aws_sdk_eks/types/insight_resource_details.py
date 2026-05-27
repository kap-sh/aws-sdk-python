"""Generated from Smithy shape ``com.amazonaws.eks#InsightResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.insight_resource_detail

InsightResourceDetails: TypeAlias = list[
    "aws_sdk_eks.types.insight_resource_detail.InsightResourceDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightResourceDetails) -> list:
    import aws_sdk_eks.types.insight_resource_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.insight_resource_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightResourceDetails:
    import aws_sdk_eks.types.insight_resource_detail

    out: InsightResourceDetails = []
    for item in data:
        out.append(aws_sdk_eks.types.insight_resource_detail.deserialize_json(item))
    return out
