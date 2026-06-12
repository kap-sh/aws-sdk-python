"""Generated from Smithy shape ``com.amazonaws.swf#ResourceTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_swf.types.resource_tag_key

ResourceTagKeyList: TypeAlias = list[
    "aws_sdk_swf.types.resource_tag_key.ResourceTagKey"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceTagKeyList:
    return list(data)
