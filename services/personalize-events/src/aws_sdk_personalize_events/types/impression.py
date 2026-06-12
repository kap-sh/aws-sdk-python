"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Impression``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.item_id

Impression: TypeAlias = list["aws_sdk_personalize_events.types.item_id.ItemId"]


# --- restJson1 ser/de ---
def serialize_json(value: Impression) -> list:
    return list(value)


def deserialize_json(data: list) -> Impression:
    return list(data)
