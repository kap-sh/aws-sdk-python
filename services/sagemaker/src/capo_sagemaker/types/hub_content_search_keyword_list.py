"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentSearchKeywordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_content_search_keyword

HubContentSearchKeywordList: TypeAlias = list[
    "capo_sagemaker.types.hub_content_search_keyword.HubContentSearchKeyword"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentSearchKeywordList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HubContentSearchKeywordList:
    return list(data)
