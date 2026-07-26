"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EventLogConfigurationListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.event_log_configuration_summary

EventLogConfigurationListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.event_log_configuration_summary.EventLogConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventLogConfigurationListDefinition) -> list:
    import capo_iot_managed_integrations.types.event_log_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.event_log_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EventLogConfigurationListDefinition:
    import capo_iot_managed_integrations.types.event_log_configuration_summary

    out: EventLogConfigurationListDefinition = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.event_log_configuration_summary.deserialize_json(
                item
            )
        )
    return out
