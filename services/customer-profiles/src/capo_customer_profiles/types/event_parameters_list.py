"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_parameters

EventParametersList: TypeAlias = list[
    "capo_customer_profiles.types.event_parameters.EventParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventParametersList) -> list:
    import capo_customer_profiles.types.event_parameters

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.event_parameters.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventParametersList:
    import capo_customer_profiles.types.event_parameters

    out: EventParametersList = []
    for item in data:
        out.append(capo_customer_profiles.types.event_parameters.deserialize_json(item))
    return out
