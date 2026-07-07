"""Generated from Smithy shape ``com.amazonaws.glue#DynamicTransform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.transform_config_parameter_list


class DynamicTransform(TypedDict, closed=True):
    name: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Specifies the name of the dynamic transform.</p>"""
    transform_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>Specifies the name of the dynamic transform as it appears in the Glue Studio visual editor.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>Specifies the inputs for the dynamic transform that are required.</p>"""
    parameters: NotRequired[
        "aws_sdk_glue.types.transform_config_parameter_list.TransformConfigParameterList"
    ]
    """<p>Specifies the parameters of the dynamic transform.</p>"""
    function_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>Specifies the name of the function of the dynamic transform.</p>"""
    path: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Specifies the path of the dynamic transform source and config files.</p>"""
    version: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>This field is not used and will be deprecated in future release.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the dynamic transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamicTransform) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["TransformName"] = value["transform_name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "parameters" in value:
        import aws_sdk_glue.types.transform_config_parameter_list

        out["Parameters"] = (
            aws_sdk_glue.types.transform_config_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    out["FunctionName"] = value["function_name"]
    out["Path"] = value["path"]
    if "version" in value:
        out["Version"] = value["version"]
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamicTransform:
    out: DynamicTransform = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DynamicTransform.name required")
    if "TransformName" in data:
        out["transform_name"] = data["TransformName"]
    else:
        raise DeserializationError("DynamicTransform.transform_name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("DynamicTransform.inputs required")
    if "Parameters" in data:
        import aws_sdk_glue.types.transform_config_parameter_list

        out["parameters"] = (
            aws_sdk_glue.types.transform_config_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError("DynamicTransform.function_name required")
    if "Path" in data:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("DynamicTransform.path required")
    if "Version" in data:
        out["version"] = data["Version"]
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
