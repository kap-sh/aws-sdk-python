"""Generated from Smithy shape ``com.amazonaws.appflow#ZendeskDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.error_handling_config
    import aws_sdk_appflow.types.id_field_name_list
    import aws_sdk_appflow.types.object
    import aws_sdk_appflow.types.write_operation_type


class ZendeskDestinationProperties(TypedDict, closed=True):
    object: "aws_sdk_appflow.types.object.Object"
    """<p>The object specified in the Zendesk flow destination.</p>"""
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
def serialize_json(value: ZendeskDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
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


def deserialize_json(data: dict) -> ZendeskDestinationProperties:
    out: ZendeskDestinationProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("ZendeskDestinationProperties.object required")
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
