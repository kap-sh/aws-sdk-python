"""Generated from Smithy shape ``com.amazonaws.kms#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.tag_key_type

TagKeyList: TypeAlias = list["capo_kms.types.tag_key_type.TagKeyType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
