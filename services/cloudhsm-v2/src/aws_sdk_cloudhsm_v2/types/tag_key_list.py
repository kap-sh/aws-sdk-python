"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.tag_key

TagKeyList: TypeAlias = list["aws_sdk_cloudhsm_v2.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyList:
    return list(data)
