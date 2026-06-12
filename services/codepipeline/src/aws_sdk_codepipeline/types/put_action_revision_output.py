"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutActionRevisionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.boolean
    import aws_sdk_codepipeline.types.pipeline_execution_id


class PutActionRevisionOutput(TypedDict):
    new_revision: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Indicates whether the artifact revision was previously used in an execution of the specified pipeline.</p>"""
    pipeline_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the current workflow state of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutActionRevisionOutput) -> dict:
    out: dict = {}
    out["newRevision"] = value.get("new_revision", False)
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutActionRevisionOutput:
    out: PutActionRevisionOutput = {}  # type: ignore[typeddict-item]
    if "newRevision" in data:
        out["new_revision"] = data["newRevision"]
    else:
        out["new_revision"] = False
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out
