"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TargetIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.target_id

TargetIdFilterList: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.target_id.TargetId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetIdFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetIdFilterList:
    return list(data)
