"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.command_endpoint

CommandEndpoints: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.command_endpoint.CommandEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandEndpoints) -> list:
    import aws_sdk_iot_managed_integrations.types.command_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.command_endpoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommandEndpoints:
    import aws_sdk_iot_managed_integrations.types.command_endpoint

    out: CommandEndpoints = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.command_endpoint.deserialize_json(
                item
            )
        )
    return out
