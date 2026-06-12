"""Generated from Smithy shape ``com.amazonaws.glue#LastActiveDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_parameter_spec
    import aws_sdk_glue.types.generic512_char_string
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.timestamp_value


class LastActiveDefinition(TypedDict):
    description: NotRequired[
        "aws_sdk_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>The description of the blueprint.</p>"""
    last_modified_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time the blueprint was last modified.</p>"""
    parameter_spec: NotRequired[
        "aws_sdk_glue.types.blueprint_parameter_spec.BlueprintParameterSpec"
    ]
    """<p>A JSON string specifying the parameters for the blueprint.</p>"""
    blueprint_location: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>Specifies a path in Amazon S3 where the blueprint is published by the Glue developer.</p>"""
    blueprint_service_location: NotRequired[
        "aws_sdk_glue.types.generic_string.GenericString"
    ]
    """<p>Specifies a path in Amazon S3 where the blueprint is copied when you create or update the blueprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastActiveDefinition) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> LastActiveDefinition:
    out: LastActiveDefinition = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
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
    return out
