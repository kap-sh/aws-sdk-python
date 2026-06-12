"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SopRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.sop_recommendation

SopRecommendationList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.sop_recommendation.SopRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SopRecommendationList) -> list:
    import aws_sdk_resiliencehub.types.sop_recommendation

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.sop_recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> SopRecommendationList:
    import aws_sdk_resiliencehub.types.sop_recommendation

    out: SopRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.sop_recommendation.deserialize_json(item)
        )
    return out
