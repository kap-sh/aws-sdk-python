"""Generated from Smithy shape ``com.amazonaws.organizations#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.tag_key

TagKeys: TypeAlias = list["capo_organizations.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeys:
    return list(data)
