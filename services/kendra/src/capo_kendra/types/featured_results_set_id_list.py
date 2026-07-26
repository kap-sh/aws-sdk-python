"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_id

FeaturedResultsSetIdList: TypeAlias = list[
    "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsSetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FeaturedResultsSetIdList:
    return list(data)
