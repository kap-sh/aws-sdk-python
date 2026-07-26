"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DestinationListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.destination_summary

DestinationListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.destination_summary.DestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationListDefinition) -> list:
    import capo_iot_managed_integrations.types.destination_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.destination_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DestinationListDefinition:
    import capo_iot_managed_integrations.types.destination_summary

    out: DestinationListDefinition = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.destination_summary.deserialize_json(
                item
            )
        )
    return out
