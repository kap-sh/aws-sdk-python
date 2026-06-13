"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationTriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.recommendation_trigger

RecommendationTriggerList: TypeAlias = list[
    "aws_sdk_qconnect.types.recommendation_trigger.RecommendationTrigger"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTriggerList) -> list:
    import aws_sdk_qconnect.types.recommendation_trigger

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.recommendation_trigger.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationTriggerList:
    import aws_sdk_qconnect.types.recommendation_trigger

    out: RecommendationTriggerList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.recommendation_trigger.deserialize_json(item))
    return out
