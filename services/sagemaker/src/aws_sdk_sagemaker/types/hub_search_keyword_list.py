"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubSearchKeywordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_search_keyword

HubSearchKeywordList: TypeAlias = list[
    "aws_sdk_sagemaker.types.hub_search_keyword.HubSearchKeyword"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubSearchKeywordList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HubSearchKeywordList:
    return list(data)
