"""Generated from Smithy shape ``com.amazonaws.groundstation#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.unbounded_string

TagKeys: TypeAlias = list["capo_groundstation.types.unbounded_string.UnboundedString"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return list(data)
