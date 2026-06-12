"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GroupBy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.group_by_attribute

GroupBy: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.group_by_attribute.GroupByAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupBy) -> list:
    import aws_sdk_resource_groups_tagging_api.types.group_by_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.group_by_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupBy:
    import aws_sdk_resource_groups_tagging_api.types.group_by_attribute

    out: GroupBy = []
    for item in data:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.group_by_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
