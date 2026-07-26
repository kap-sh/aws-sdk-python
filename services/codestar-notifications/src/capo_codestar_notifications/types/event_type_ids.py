"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#EventTypeIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_notifications.types.event_type_id

EventTypeIds: TypeAlias = list[
    "capo_codestar_notifications.types.event_type_id.EventTypeId"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventTypeIds) -> list:
    return list(value)


def deserialize_json(data: list) -> EventTypeIds:
    return list(data)
