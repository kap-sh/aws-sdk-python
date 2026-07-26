"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVariableDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_variable_description
    import capo_codepipeline.types.pipeline_variable_name
    import capo_codepipeline.types.pipeline_variable_value


class PipelineVariableDeclaration(TypedDict, closed=True):
    name: "capo_codepipeline.types.pipeline_variable_name.PipelineVariableName"
    """<p>The name of a pipeline-level variable.</p>"""
    default_value: NotRequired[
        "capo_codepipeline.types.pipeline_variable_value.PipelineVariableValue"
    ]
    """<p>The value of a pipeline-level variable.</p>"""
    description: NotRequired[
        "capo_codepipeline.types.pipeline_variable_description.PipelineVariableDescription"
    ]
    """<p>The description of a pipeline-level variable. It's used to add additional context about the variable, and not being used at time when pipeline executes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVariableDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVariableDeclaration:
    out: PipelineVariableDeclaration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PipelineVariableDeclaration.name required")
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "description" in data:
        out["description"] = data["description"]
    return out
