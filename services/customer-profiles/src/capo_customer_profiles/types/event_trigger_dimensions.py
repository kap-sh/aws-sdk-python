"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_trigger_dimension

EventTriggerDimensions: TypeAlias = list[
    "capo_customer_profiles.types.event_trigger_dimension.EventTriggerDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerDimensions) -> list:
    import capo_customer_profiles.types.event_trigger_dimension

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.event_trigger_dimension.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventTriggerDimensions:
    import capo_customer_profiles.types.event_trigger_dimension

    out: EventTriggerDimensions = []
    for item in data:
        out.append(
            capo_customer_profiles.types.event_trigger_dimension.deserialize_json(item)
        )
    return out
