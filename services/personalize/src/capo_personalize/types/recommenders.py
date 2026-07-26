"""Generated from Smithy shape ``com.amazonaws.personalize#Recommenders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.recommender_summary

Recommenders: TypeAlias = list[
    "capo_personalize.types.recommender_summary.RecommenderSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommenders) -> list:
    import capo_personalize.types.recommender_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.recommender_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Recommenders:
    import capo_personalize.types.recommender_summary

    out: Recommenders = []
    for item in data:
        out.append(
            capo_personalize.types.recommender_summary.deserialize_aws_json_1_1(item)
        )
    return out
