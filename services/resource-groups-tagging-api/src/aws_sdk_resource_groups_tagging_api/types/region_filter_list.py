"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#RegionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.region

RegionFilterList: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.region.Region"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RegionFilterList:
    return list(data)
