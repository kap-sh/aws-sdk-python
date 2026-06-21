"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobsSortBy``."""

from typing import Literal, TypeAlias, cast

ListInferenceRecommendationsJobsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListInferenceRecommendationsJobsSortBy:
    return cast(ListInferenceRecommendationsJobsSortBy, data)
