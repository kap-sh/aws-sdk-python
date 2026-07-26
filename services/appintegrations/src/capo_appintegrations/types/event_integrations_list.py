"""Generated from Smithy shape ``com.amazonaws.appintegrations#EventIntegrationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appintegrations.types.event_integration

EventIntegrationsList: TypeAlias = list[
    "capo_appintegrations.types.event_integration.EventIntegration"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventIntegrationsList) -> list:
    import capo_appintegrations.types.event_integration

    out: list = []
    for item in value:
        out.append(capo_appintegrations.types.event_integration.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventIntegrationsList:
    import capo_appintegrations.types.event_integration

    out: EventIntegrationsList = []
    for item in data:
        out.append(capo_appintegrations.types.event_integration.deserialize_json(item))
    return out
