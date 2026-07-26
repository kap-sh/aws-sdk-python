"""Generated from Smithy shape ``com.amazonaws.medialive#__listOf__integer``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.__integer

__listOf__integer: TypeAlias = list["capo_medialive.types.__integer.__integer"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__integer) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__integer:
    return list(data)
