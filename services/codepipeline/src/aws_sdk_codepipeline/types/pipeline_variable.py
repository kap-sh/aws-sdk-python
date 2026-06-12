"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVariable``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_variable_name
    import aws_sdk_codepipeline.types.pipeline_variable_value


class PipelineVariable(TypedDict):
    name: "aws_sdk_codepipeline.types.pipeline_variable_name.PipelineVariableName"
    """<p>The name of a pipeline-level variable.</p>"""
    value: "aws_sdk_codepipeline.types.pipeline_variable_value.PipelineVariableValue"
    """<p>The value of a pipeline-level variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVariable:
    out: PipelineVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PipelineVariable.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("PipelineVariable.value required")
    return out
