"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.command_capability

CommandCapabilities: TypeAlias = list[
    "capo_iot_managed_integrations.types.command_capability.CommandCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandCapabilities) -> list:
    import capo_iot_managed_integrations.types.command_capability

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.command_capability.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommandCapabilities:
    import capo_iot_managed_integrations.types.command_capability

    out: CommandCapabilities = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.command_capability.deserialize_json(
                item
            )
        )
    return out
