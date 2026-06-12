"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AlarmRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.alarm_recommendation

AlarmRecommendationList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.alarm_recommendation.AlarmRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmRecommendationList) -> list:
    import aws_sdk_resiliencehub.types.alarm_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.alarm_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AlarmRecommendationList:
    import aws_sdk_resiliencehub.types.alarm_recommendation

    out: AlarmRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.alarm_recommendation.deserialize_json(item)
        )
    return out
