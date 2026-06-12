"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceTagMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping

ResourceTagMappingList: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping.ResourceTagMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagMappingList) -> list:
    import aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceTagMappingList:
    import aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping

    out: ResourceTagMappingList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
