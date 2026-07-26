"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Impression``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.item_id

Impression: TypeAlias = list["capo_personalize_events.types.item_id.ItemId"]


# --- restJson1 ser/de ---
def serialize_json(value: Impression) -> list:
    return list(value)


def deserialize_json(data: list) -> Impression:
    return list(data)
