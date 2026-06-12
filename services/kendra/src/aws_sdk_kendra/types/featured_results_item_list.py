"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.featured_results_item

FeaturedResultsItemList: TypeAlias = list[
    "aws_sdk_kendra.types.featured_results_item.FeaturedResultsItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsItemList) -> list:
    import aws_sdk_kendra.types.featured_results_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.featured_results_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeaturedResultsItemList:
    import aws_sdk_kendra.types.featured_results_item

    out: FeaturedResultsItemList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.featured_results_item.deserialize_aws_json_1_1(item)
        )
    return out
