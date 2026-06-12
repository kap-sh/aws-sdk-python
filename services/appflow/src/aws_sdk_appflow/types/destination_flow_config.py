"""Generated from Smithy shape ``com.amazonaws.appflow#DestinationFlowConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.api_version
    import aws_sdk_appflow.types.connector_profile_name
    import aws_sdk_appflow.types.connector_type
    import aws_sdk_appflow.types.destination_connector_properties


class DestinationFlowConfig(TypedDict):
    connector_type: "aws_sdk_appflow.types.connector_type.ConnectorType"
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    api_version: NotRequired["aws_sdk_appflow.types.api_version.ApiVersion"]
    """<p>The API version that the destination connector uses.</p>"""
    connector_profile_name: NotRequired[
        "aws_sdk_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p> The name of the connector profile. This name must be unique for each connector profile in the Amazon Web Services account. </p>"""
    destination_connector_properties: "aws_sdk_appflow.types.destination_connector_properties.DestinationConnectorProperties"
    """<p> This stores the information that is required to query a particular connector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationFlowConfig) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.connector_type

    out["connectorType"] = aws_sdk_appflow.types.connector_type.serialize_json(
        value["connector_type"]
    )
    if "api_version" in value:
        out["apiVersion"] = value["api_version"]
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    import aws_sdk_appflow.types.destination_connector_properties

    out["destinationConnectorProperties"] = (
        aws_sdk_appflow.types.destination_connector_properties.serialize_json(
            value["destination_connector_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> DestinationFlowConfig:
    out: DestinationFlowConfig = {}  # type: ignore[typeddict-item]
    if "connectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["connector_type"] = aws_sdk_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    else:
        raise DeserializationError("DestinationFlowConfig.connector_type required")
    if "apiVersion" in data:
        out["api_version"] = data["apiVersion"]
    if "connectorProfileName" in data:
        out["connector_profile_name"] = data["connectorProfileName"]
    if "destinationConnectorProperties" in data:
        import aws_sdk_appflow.types.destination_connector_properties

        out["destination_connector_properties"] = (
            aws_sdk_appflow.types.destination_connector_properties.deserialize_json(
                data["destinationConnectorProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DestinationFlowConfig.destination_connector_properties required"
        )
    return out
