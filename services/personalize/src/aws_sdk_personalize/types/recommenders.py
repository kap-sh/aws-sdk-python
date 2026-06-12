"""Generated from Smithy shape ``com.amazonaws.personalize#Recommenders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.recommender_summary

Recommenders: TypeAlias = list[
    "aws_sdk_personalize.types.recommender_summary.RecommenderSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommenders) -> list:
    import aws_sdk_personalize.types.recommender_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.recommender_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Recommenders:
    import aws_sdk_personalize.types.recommender_summary

    out: Recommenders = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.recommender_summary.deserialize_aws_json_1_1(item)
        )
    return out
