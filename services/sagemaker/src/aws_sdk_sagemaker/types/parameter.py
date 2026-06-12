"""Generated from Smithy shape ``com.amazonaws.sagemaker#Parameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_parameter_name
    import aws_sdk_sagemaker.types.string1024


class Parameter(TypedDict):
    name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_parameter_name.PipelineParameterName"
    ]
    """<p>The name of the parameter to assign a value to. This parameter name must match a named parameter in the pipeline definition.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The literal value for the parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
