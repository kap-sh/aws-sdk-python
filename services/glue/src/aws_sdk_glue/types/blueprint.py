"""Generated from Smithy shape ``com.amazonaws.glue#Blueprint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_parameter_spec
    import aws_sdk_glue.types.blueprint_status
    import aws_sdk_glue.types.error_string
    import aws_sdk_glue.types.generic512_char_string
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.last_active_definition
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.timestamp_value


class Blueprint(TypedDict):
    name: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The name of the blueprint.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>The description of the blueprint.</p>"""
    created_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time the blueprint was registered.</p>"""
    last_modified_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time the blueprint was last modified.</p>"""
    parameter_spec: NotRequired[
        "aws_sdk_glue.types.blueprint_parameter_spec.BlueprintParameterSpec"
    ]
    """<p>A JSON string that indicates the list of parameter specifications for the blueprint.</p>"""
    blueprint_location: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>Specifies the path in Amazon S3 where the blueprint is published.</p>"""
    blueprint_service_location: NotRequired[
        "aws_sdk_glue.types.generic_string.GenericString"
    ]
    """<p>Specifies a path in Amazon S3 where the blueprint is copied when you call <code>CreateBlueprint/UpdateBlueprint</code> to register the blueprint in Glue.</p>"""
    status: NotRequired["aws_sdk_glue.types.blueprint_status.BlueprintStatus"]
    """<p>The status of the blueprint registration.</p> <ul> <li> <p>Creating — The blueprint registration is in progress.</p> </li> <li> <p>Active — The blueprint has been successfully registered.</p> </li> <li> <p>Updating — An update to the blueprint registration is in progress.</p> </li> <li> <p>Failed — The blueprint registration failed.</p> </li> </ul>"""
    error_message: NotRequired["aws_sdk_glue.types.error_string.ErrorString"]
    """<p>An error message.</p>"""
    last_active_definition: NotRequired[
        "aws_sdk_glue.types.last_active_definition.LastActiveDefinition"
    ]
    """<p>When there are multiple versions of a blueprint and the latest version has some errors, this attribute indicates the last successful blueprint definition that is available with the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Blueprint) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CreatedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "last_modified_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["LastModifiedOn"] = (
            aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["last_modified_on"]
            )
        )
    if "parameter_spec" in value:
        out["ParameterSpec"] = value["parameter_spec"]
    if "blueprint_location" in value:
        out["BlueprintLocation"] = value["blueprint_location"]
    if "blueprint_service_location" in value:
        out["BlueprintServiceLocation"] = value["blueprint_service_location"]
    if "status" in value:
        import aws_sdk_glue.types.blueprint_status

        out["Status"] = aws_sdk_glue.types.blueprint_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "last_active_definition" in value:
        import aws_sdk_glue.types.last_active_definition

        out["LastActiveDefinition"] = (
            aws_sdk_glue.types.last_active_definition.serialize_aws_json_1_1(
                value["last_active_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Blueprint:
    out: Blueprint = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["created_on"] = aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if "LastModifiedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["last_modified_on"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["LastModifiedOn"]
            )
        )
    if "ParameterSpec" in data:
        out["parameter_spec"] = data["ParameterSpec"]
    if "BlueprintLocation" in data:
        out["blueprint_location"] = data["BlueprintLocation"]
    if "BlueprintServiceLocation" in data:
        out["blueprint_service_location"] = data["BlueprintServiceLocation"]
    if "Status" in data:
        import aws_sdk_glue.types.blueprint_status

        out["status"] = aws_sdk_glue.types.blueprint_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LastActiveDefinition" in data:
        import aws_sdk_glue.types.last_active_definition

        out["last_active_definition"] = (
            aws_sdk_glue.types.last_active_definition.deserialize_aws_json_1_1(
                data["LastActiveDefinition"]
            )
        )
    return out
