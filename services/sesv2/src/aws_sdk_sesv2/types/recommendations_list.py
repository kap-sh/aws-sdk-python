"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.recommendation

RecommendationsList: TypeAlias = list[
    "aws_sdk_sesv2.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationsList) -> list:
    import aws_sdk_sesv2.types.recommendation

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationsList:
    import aws_sdk_sesv2.types.recommendation

    out: RecommendationsList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.recommendation.deserialize_json(item))
    return out
