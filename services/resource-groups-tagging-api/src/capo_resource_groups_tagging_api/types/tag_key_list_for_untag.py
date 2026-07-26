"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagKeyListForUntag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_key

TagKeyListForUntag: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.tag_key.TagKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyListForUntag) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyListForUntag:
    return list(data)
