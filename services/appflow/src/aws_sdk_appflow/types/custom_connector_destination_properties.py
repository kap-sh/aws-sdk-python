"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.custom_properties
    import aws_sdk_appflow.types.entity_name
    import aws_sdk_appflow.types.error_handling_config
    import aws_sdk_appflow.types.id_field_name_list
    import aws_sdk_appflow.types.write_operation_type


class CustomConnectorDestinationProperties(TypedDict, closed=True):
    entity_name: "aws_sdk_appflow.types.entity_name.EntityName"
    """<p>The entity specified in the custom connector as a destination in the flow.</p>"""
    error_handling_config: NotRequired[
        "aws_sdk_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    """<p>The settings that determine how Amazon AppFlow handles an error when placing data in the custom connector as destination.</p>"""
    write_operation_type: NotRequired[
        "aws_sdk_appflow.types.write_operation_type.WriteOperationType"
    ]
    """<p>Specifies the type of write operation to be performed in the custom connector when it's used as destination.</p>"""
    id_field_names: NotRequired[
        "aws_sdk_appflow.types.id_field_name_list.IdFieldNameList"
    ]
    """<p>The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update, delete, or upsert.</p>"""
    custom_properties: NotRequired[
        "aws_sdk_appflow.types.custom_properties.CustomProperties"
    ]
    """<p>The custom properties that are specific to the connector when it's used as a destination in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorDestinationProperties) -> dict:
    out: dict = {}
    out["entityName"] = value["entity_name"]
    if "error_handling_config" in value:
        import aws_sdk_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            aws_sdk_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    if "write_operation_type" in value:
        import aws_sdk_appflow.types.write_operation_type

        out["writeOperationType"] = (
            aws_sdk_appflow.types.write_operation_type.serialize_json(
                value["write_operation_type"]
            )
        )
    if "id_field_names" in value:
        import aws_sdk_appflow.types.id_field_name_list

        out["idFieldNames"] = aws_sdk_appflow.types.id_field_name_list.serialize_json(
            value["id_field_names"]
        )
    if "custom_properties" in value:
        import aws_sdk_appflow.types.custom_properties

        out["customProperties"] = (
            aws_sdk_appflow.types.custom_properties.serialize_json(
                value["custom_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorDestinationProperties:
    out: CustomConnectorDestinationProperties = {}  # type: ignore[typeddict-item]
    if "entityName" in data:
        out["entity_name"] = data["entityName"]
    else:
        raise DeserializationError(
            "CustomConnectorDestinationProperties.entity_name required"
        )
    if "errorHandlingConfig" in data:
        import aws_sdk_appflow.types.error_handling_config

        out["error_handling_config"] = (
            aws_sdk_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    if "writeOperationType" in data:
        import aws_sdk_appflow.types.write_operation_type

        out["write_operation_type"] = (
            aws_sdk_appflow.types.write_operation_type.deserialize_json(
                data["writeOperationType"]
            )
        )
    if "idFieldNames" in data:
        import aws_sdk_appflow.types.id_field_name_list

        out["id_field_names"] = (
            aws_sdk_appflow.types.id_field_name_list.deserialize_json(
                data["idFieldNames"]
            )
        )
    if "customProperties" in data:
        import aws_sdk_appflow.types.custom_properties

        out["custom_properties"] = (
            aws_sdk_appflow.types.custom_properties.deserialize_json(
                data["customProperties"]
            )
        )
    return out
