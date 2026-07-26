"""Generated from Smithy shape ``com.amazonaws.pcs#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.tag_key

TagKeys: TypeAlias = list["capo_pcs.types.tag_key.TagKey"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TagKeys:
    return list(data)
