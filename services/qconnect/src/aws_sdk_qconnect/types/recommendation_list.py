"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.recommendation_data

RecommendationList: TypeAlias = list[
    "aws_sdk_qconnect.types.recommendation_data.RecommendationData"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationList) -> list:
    import aws_sdk_qconnect.types.recommendation_data

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.recommendation_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationList:
    import aws_sdk_qconnect.types.recommendation_data

    out: RecommendationList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.recommendation_data.deserialize_json(item))
    return out
