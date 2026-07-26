"""Generated from Smithy shape ``com.amazonaws.eks#InsightResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.insight_resource_detail

InsightResourceDetails: TypeAlias = list[
    "capo_eks.types.insight_resource_detail.InsightResourceDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightResourceDetails) -> list:
    import capo_eks.types.insight_resource_detail

    out: list = []
    for item in value:
        out.append(capo_eks.types.insight_resource_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightResourceDetails:
    import capo_eks.types.insight_resource_detail

    out: InsightResourceDetails = []
    for item in data:
        out.append(capo_eks.types.insight_resource_detail.deserialize_json(item))
    return out
