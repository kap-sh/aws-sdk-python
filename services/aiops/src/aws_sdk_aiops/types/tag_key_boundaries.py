"""Generated from Smithy shape ``com.amazonaws.aiops#TagKeyBoundaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_aiops.types.tag_key

TagKeyBoundaries: TypeAlias = list["aws_sdk_aiops.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyBoundaries) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyBoundaries:
    return list(data)
