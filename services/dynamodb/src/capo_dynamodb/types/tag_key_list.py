"""Generated from Smithy shape ``com.amazonaws.dynamodb#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.tag_key_string

TagKeyList: TypeAlias = list["capo_dynamodb.types.tag_key_string.TagKeyString"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
