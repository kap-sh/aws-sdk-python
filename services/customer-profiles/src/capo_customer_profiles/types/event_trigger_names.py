"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.name

EventTriggerNames: TypeAlias = list["capo_customer_profiles.types.name.name"]


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerNames) -> list:
    return list(value)


def deserialize_json(data: list) -> EventTriggerNames:
    return list(data)
