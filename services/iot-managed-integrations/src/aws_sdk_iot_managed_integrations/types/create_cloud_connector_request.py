"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateCloudConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.cloud_connector_description
    import aws_sdk_iot_managed_integrations.types.display_name
    import aws_sdk_iot_managed_integrations.types.endpoint_config
    import aws_sdk_iot_managed_integrations.types.endpoint_type


class CreateCloudConnectorRequest(TypedDict):
    name: "aws_sdk_iot_managed_integrations.types.display_name.DisplayName"
    """<p>The display name of the C2C connector.</p>"""
    endpoint_config: (
        "aws_sdk_iot_managed_integrations.types.endpoint_config.EndpointConfig"
    )
    """<p>The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
    ]
    """<p>A description of the C2C connector.</p>"""
    endpoint_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.endpoint_type.EndpointType"
    ]
    """<p>The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.</p>"""
    client_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_iot_managed_integrations.types.endpoint_config

    out["EndpointConfig"] = (
        aws_sdk_iot_managed_integrations.types.endpoint_config.serialize_json(
            value["endpoint_config"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "endpoint_type" in value:
        import aws_sdk_iot_managed_integrations.types.endpoint_type

        out["EndpointType"] = (
            aws_sdk_iot_managed_integrations.types.endpoint_type.serialize_json(
                value["endpoint_type"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCloudConnectorRequest:
    out: CreateCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCloudConnectorRequest.name required")
    if "EndpointConfig" in data:
        import aws_sdk_iot_managed_integrations.types.endpoint_config

        out["endpoint_config"] = (
            aws_sdk_iot_managed_integrations.types.endpoint_config.deserialize_json(
                data["EndpointConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCloudConnectorRequest.endpoint_config required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "EndpointType" in data:
        import aws_sdk_iot_managed_integrations.types.endpoint_type

        out["endpoint_type"] = (
            aws_sdk_iot_managed_integrations.types.endpoint_type.deserialize_json(
                data["EndpointType"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
