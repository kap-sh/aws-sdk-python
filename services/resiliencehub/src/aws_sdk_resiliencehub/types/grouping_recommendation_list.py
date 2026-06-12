"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.grouping_recommendation

GroupingRecommendationList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.grouping_recommendation.GroupingRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingRecommendationList) -> list:
    import aws_sdk_resiliencehub.types.grouping_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.grouping_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GroupingRecommendationList:
    import aws_sdk_resiliencehub.types.grouping_recommendation

    out: GroupingRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.grouping_recommendation.deserialize_json(item)
        )
    return out
