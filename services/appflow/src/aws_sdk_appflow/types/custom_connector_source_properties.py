"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.custom_properties
    import aws_sdk_appflow.types.data_transfer_api
    import aws_sdk_appflow.types.entity_name


class CustomConnectorSourceProperties(TypedDict):
    entity_name: "aws_sdk_appflow.types.entity_name.EntityName"
    """<p>The entity specified in the custom connector as a source in the flow.</p>"""
    custom_properties: NotRequired[
        "aws_sdk_appflow.types.custom_properties.CustomProperties"
    ]
    """<p>Custom properties that are required to use the custom connector as a source.</p>"""
    data_transfer_api: NotRequired[
        "aws_sdk_appflow.types.data_transfer_api.DataTransferApi"
    ]
    """<p>The API of the connector application that Amazon AppFlow uses to transfer your data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorSourceProperties) -> dict:
    out: dict = {}
    out["entityName"] = value["entity_name"]
    if "custom_properties" in value:
        import aws_sdk_appflow.types.custom_properties

        out["customProperties"] = (
            aws_sdk_appflow.types.custom_properties.serialize_json(
                value["custom_properties"]
            )
        )
    if "data_transfer_api" in value:
        import aws_sdk_appflow.types.data_transfer_api

        out["dataTransferApi"] = aws_sdk_appflow.types.data_transfer_api.serialize_json(
            value["data_transfer_api"]
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorSourceProperties:
    out: CustomConnectorSourceProperties = {}  # type: ignore[typeddict-item]
    if "entityName" in data:
        out["entity_name"] = data["entityName"]
    else:
        raise DeserializationError(
            "CustomConnectorSourceProperties.entity_name required"
        )
    if "customProperties" in data:
        import aws_sdk_appflow.types.custom_properties

        out["custom_properties"] = (
            aws_sdk_appflow.types.custom_properties.deserialize_json(
                data["customProperties"]
            )
        )
    if "dataTransferApi" in data:
        import aws_sdk_appflow.types.data_transfer_api

        out["data_transfer_api"] = (
            aws_sdk_appflow.types.data_transfer_api.deserialize_json(
                data["dataTransferApi"]
            )
        )
    return out
