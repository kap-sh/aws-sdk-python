"""Generated from Smithy shape ``com.amazonaws.lakeformation#TagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_value

TagValueList: TypeAlias = list["aws_sdk_lakeformation.types.lf_tag_value.LFTagValue"]


# --- restJson1 ser/de ---
def serialize_json(value: TagValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagValueList:
    return list(data)
