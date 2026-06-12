"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataDestinationProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.error_handling_config
    import aws_sdk_appflow.types.id_field_name_list
    import aws_sdk_appflow.types.object
    import aws_sdk_appflow.types.success_response_handling_config
    import aws_sdk_appflow.types.write_operation_type


class SAPODataDestinationProperties(TypedDict):
    object_path: "aws_sdk_appflow.types.object.Object"
    """<p>The object path specified in the SAPOData flow destination.</p>"""
    success_response_handling_config: NotRequired[
        "aws_sdk_appflow.types.success_response_handling_config.SuccessResponseHandlingConfig"
    ]
    """<p>Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.</p> <p>For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.</p>"""
    id_field_names: NotRequired[
        "aws_sdk_appflow.types.id_field_name_list.IdFieldNameList"
    ]
    error_handling_config: NotRequired[
        "aws_sdk_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    write_operation_type: NotRequired[
        "aws_sdk_appflow.types.write_operation_type.WriteOperationType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataDestinationProperties) -> dict:
    out: dict = {}
    out["objectPath"] = value["object_path"]
    if "success_response_handling_config" in value:
        import aws_sdk_appflow.types.success_response_handling_config

        out["successResponseHandlingConfig"] = (
            aws_sdk_appflow.types.success_response_handling_config.serialize_json(
                value["success_response_handling_config"]
            )
        )
    if "id_field_names" in value:
        import aws_sdk_appflow.types.id_field_name_list

        out["idFieldNames"] = aws_sdk_appflow.types.id_field_name_list.serialize_json(
            value["id_field_names"]
        )
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
    return out


def deserialize_json(data: dict) -> SAPODataDestinationProperties:
    out: SAPODataDestinationProperties = {}  # type: ignore[typeddict-item]
    if "objectPath" in data:
        out["object_path"] = data["objectPath"]
    else:
        raise DeserializationError("SAPODataDestinationProperties.object_path required")
    if "successResponseHandlingConfig" in data:
        import aws_sdk_appflow.types.success_response_handling_config

        out["success_response_handling_config"] = (
            aws_sdk_appflow.types.success_response_handling_config.deserialize_json(
                data["successResponseHandlingConfig"]
            )
        )
    if "idFieldNames" in data:
        import aws_sdk_appflow.types.id_field_name_list

        out["id_field_names"] = (
            aws_sdk_appflow.types.id_field_name_list.deserialize_json(
                data["idFieldNames"]
            )
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
    return out
