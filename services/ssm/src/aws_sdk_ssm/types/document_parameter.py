"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_parameter_default_value
    import aws_sdk_ssm.types.document_parameter_descrption
    import aws_sdk_ssm.types.document_parameter_name
    import aws_sdk_ssm.types.document_parameter_type


class DocumentParameter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ssm.types.document_parameter_name.DocumentParameterName"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["aws_sdk_ssm.types.document_parameter_type.DocumentParameterType"]
    """<p>The type of parameter. The type can be either String or StringList.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.document_parameter_descrption.DocumentParameterDescrption"
    ]
    """<p>A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.</p>"""
    default_value: NotRequired[
        "aws_sdk_ssm.types.document_parameter_default_value.DocumentParameterDefaultValue"
    ]
    """<p>If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_ssm.types.document_parameter_type

        out["Type"] = aws_sdk_ssm.types.document_parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentParameter:
    out: DocumentParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_ssm.types.document_parameter_type

        out["type"] = (
            aws_sdk_ssm.types.document_parameter_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    return out
