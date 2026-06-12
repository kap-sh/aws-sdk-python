"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceARNListForGet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.resource_arn

ResourceARNListForGet: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.resource_arn.ResourceARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceARNListForGet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceARNListForGet:
    return list(data)
