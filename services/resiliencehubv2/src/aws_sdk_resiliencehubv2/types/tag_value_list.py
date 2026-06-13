"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.tag_value

TagValueList: TypeAlias = list["aws_sdk_resiliencehubv2.types.tag_value.TagValue"]


# --- restJson1 ser/de ---
def serialize_json(value: TagValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagValueList:
    return list(data)
