"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ReportingTagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_key

ReportingTagKeys: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.tag_key.TagKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportingTagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReportingTagKeys:
    return list(data)
