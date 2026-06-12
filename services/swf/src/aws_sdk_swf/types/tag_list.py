"""Generated from Smithy shape ``com.amazonaws.swf#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_swf.types.tag

TagList: TypeAlias = list["aws_sdk_swf.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TagList:
    return list(data)
