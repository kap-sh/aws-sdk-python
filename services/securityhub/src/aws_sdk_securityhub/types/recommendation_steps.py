"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.recommendation_step

RecommendationSteps: TypeAlias = list[
    "aws_sdk_securityhub.types.recommendation_step.RecommendationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSteps) -> list:
    import aws_sdk_securityhub.types.recommendation_step

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.recommendation_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationSteps:
    import aws_sdk_securityhub.types.recommendation_step

    out: RecommendationSteps = []
    for item in data:
        out.append(aws_sdk_securityhub.types.recommendation_step.deserialize_json(item))
    return out
