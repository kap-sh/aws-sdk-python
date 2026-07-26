"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.test_recommendation

TestRecommendationList: TypeAlias = list[
    "capo_resiliencehub.types.test_recommendation.TestRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRecommendationList) -> list:
    import capo_resiliencehub.types.test_recommendation

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.test_recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestRecommendationList:
    import capo_resiliencehub.types.test_recommendation

    out: TestRecommendationList = []
    for item in data:
        out.append(capo_resiliencehub.types.test_recommendation.deserialize_json(item))
    return out
