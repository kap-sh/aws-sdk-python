"""Generated from Smithy shape ``com.amazonaws.glacier#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string

TagKeyList: TypeAlias = list["aws_sdk_glacier.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return list(data)
