"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.command_capabilities
    import aws_sdk_iot_managed_integrations.types.endpoint_id


class CommandEndpoint(TypedDict):
    endpoint_id: "aws_sdk_iot_managed_integrations.types.endpoint_id.EndpointId"
    """<p>The id of the endpoint for a managed thing.</p>"""
    capabilities: "aws_sdk_iot_managed_integrations.types.command_capabilities.CommandCapabilities"
    """<p>Describe the endpoint with an id, a name, and the relevant capabilities for sending commands.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandEndpoint) -> dict:
    out: dict = {}
    out["endpointId"] = value["endpoint_id"]
    import aws_sdk_iot_managed_integrations.types.command_capabilities

    out["capabilities"] = (
        aws_sdk_iot_managed_integrations.types.command_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> CommandEndpoint:
    out: CommandEndpoint = {}  # type: ignore[typeddict-item]
    if "endpointId" in data:
        out["endpoint_id"] = data["endpointId"]
    else:
        raise DeserializationError("CommandEndpoint.endpoint_id required")
    if "capabilities" in data:
        import aws_sdk_iot_managed_integrations.types.command_capabilities

        out["capabilities"] = (
            aws_sdk_iot_managed_integrations.types.command_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    else:
        raise DeserializationError("CommandEndpoint.capabilities required")
    return out
