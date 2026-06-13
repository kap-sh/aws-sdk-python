"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestingRecommendationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.testing_recommendation

TestingRecommendationsList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.testing_recommendation.TestingRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestingRecommendationsList) -> list:
    import aws_sdk_resiliencehubv2.types.testing_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.testing_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestingRecommendationsList:
    import aws_sdk_resiliencehubv2.types.testing_recommendation

    out: TestingRecommendationsList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.testing_recommendation.deserialize_json(item)
        )
    return out
