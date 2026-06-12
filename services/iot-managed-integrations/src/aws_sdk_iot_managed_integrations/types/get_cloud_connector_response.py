"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCloudConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.cloud_connector_description
    import aws_sdk_iot_managed_integrations.types.cloud_connector_id
    import aws_sdk_iot_managed_integrations.types.cloud_connector_type
    import aws_sdk_iot_managed_integrations.types.display_name
    import aws_sdk_iot_managed_integrations.types.endpoint_config
    import aws_sdk_iot_managed_integrations.types.endpoint_type


class GetCloudConnectorResponse(TypedDict):
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
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The unique identifier of the cloud connector.</p>"""
    type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
    ]
    """<p>The type of cloud connector created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudConnectorResponse) -> dict:
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
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_iot_managed_integrations.types.cloud_connector_type

        out["Type"] = (
            aws_sdk_iot_managed_integrations.types.cloud_connector_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCloudConnectorResponse:
    out: GetCloudConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetCloudConnectorResponse.name required")
    if "EndpointConfig" in data:
        import aws_sdk_iot_managed_integrations.types.endpoint_config

        out["endpoint_config"] = (
            aws_sdk_iot_managed_integrations.types.endpoint_config.deserialize_json(
                data["EndpointConfig"]
            )
        )
    else:
        raise DeserializationError("GetCloudConnectorResponse.endpoint_config required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "EndpointType" in data:
        import aws_sdk_iot_managed_integrations.types.endpoint_type

        out["endpoint_type"] = (
            aws_sdk_iot_managed_integrations.types.endpoint_type.deserialize_json(
                data["EndpointType"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_iot_managed_integrations.types.cloud_connector_type

        out["type"] = (
            aws_sdk_iot_managed_integrations.types.cloud_connector_type.deserialize_json(
                data["Type"]
            )
        )
    return out
