"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#RequiredTagsForListRequiredTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.required_tag

RequiredTagsForListRequiredTags: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.required_tag.RequiredTag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequiredTagsForListRequiredTags) -> list:
    import aws_sdk_resource_groups_tagging_api.types.required_tag

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.required_tag.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RequiredTagsForListRequiredTags:
    import aws_sdk_resource_groups_tagging_api.types.required_tag

    out: RequiredTagsForListRequiredTags = []
    for item in data:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.required_tag.deserialize_aws_json_1_1(
                item
            )
        )
    return out
