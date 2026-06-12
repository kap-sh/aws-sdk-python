"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.command_capability

CommandCapabilities: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.command_capability.CommandCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandCapabilities) -> list:
    import aws_sdk_iot_managed_integrations.types.command_capability

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.command_capability.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CommandCapabilities:
    import aws_sdk_iot_managed_integrations.types.command_capability

    out: CommandCapabilities = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.command_capability.deserialize_json(
                item
            )
        )
    return out
