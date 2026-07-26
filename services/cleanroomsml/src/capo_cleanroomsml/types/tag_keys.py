"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.tag_key

TagKeys: TypeAlias = list["capo_cleanroomsml.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return list(data)
