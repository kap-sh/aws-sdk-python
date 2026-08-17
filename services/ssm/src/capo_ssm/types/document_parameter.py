"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_parameter_default_value
    import capo_ssm.types.document_parameter_descrption
    import capo_ssm.types.document_parameter_name
    import capo_ssm.types.document_parameter_type


class DocumentParameter(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.document_parameter_name.DocumentParameterName"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["capo_ssm.types.document_parameter_type.DocumentParameterType"]
    """<p>The type of parameter. The type can be either String or StringList.</p>"""
    description: NotRequired[
        "capo_ssm.types.document_parameter_descrption.DocumentParameterDescrption"
    ]
    """<p>A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.</p>"""
    default_value: NotRequired[
        "capo_ssm.types.document_parameter_default_value.DocumentParameterDefaultValue"
    ]
    """<p>If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_ssm.types.document_parameter_type

        out["Type"] = capo_ssm.types.document_parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentParameter:
    out: DocumentParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_ssm.types.document_parameter_type

        out["type"] = capo_ssm.types.document_parameter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    return out
