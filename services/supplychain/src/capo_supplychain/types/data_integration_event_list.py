"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_event

DataIntegrationEventList: TypeAlias = list[
    "capo_supplychain.types.data_integration_event.DataIntegrationEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventList) -> list:
    import capo_supplychain.types.data_integration_event

    out: list = []
    for item in value:
        out.append(capo_supplychain.types.data_integration_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataIntegrationEventList:
    import capo_supplychain.types.data_integration_event

    out: DataIntegrationEventList = []
    for item in data:
        out.append(capo_supplychain.types.data_integration_event.deserialize_json(item))
    return out
