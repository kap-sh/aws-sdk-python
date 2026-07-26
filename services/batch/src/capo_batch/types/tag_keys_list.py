"""Generated from Smithy shape ``com.amazonaws.batch#TagKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.tag_key

TagKeysList: TypeAlias = list["capo_batch.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeysList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeysList:
    return list(data)
