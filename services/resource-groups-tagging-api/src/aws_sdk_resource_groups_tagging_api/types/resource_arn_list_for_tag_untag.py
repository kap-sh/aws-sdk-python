"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceARNListForTagUntag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.resource_arn

ResourceARNListForTagUntag: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.resource_arn.ResourceARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceARNListForTagUntag) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceARNListForTagUntag:
    return list(data)
