"""Generated from Smithy shape ``com.amazonaws.glue#TagKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.tag_key

TagKeysList: TypeAlias = list["capo_glue.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeysList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeysList:
    return list(data)
