"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineRollbackMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_execution_id


class PipelineRollbackMetadata(TypedDict):
    rollback_target_pipeline_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The pipeline execution ID to which the stage will be rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineRollbackMetadata) -> dict:
    out: dict = {}
    if "rollback_target_pipeline_execution_id" in value:
        out["rollbackTargetPipelineExecutionId"] = value[
            "rollback_target_pipeline_execution_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineRollbackMetadata:
    out: PipelineRollbackMetadata = {}  # type: ignore[typeddict-item]
    if "rollbackTargetPipelineExecutionId" in data:
        out["rollback_target_pipeline_execution_id"] = data[
            "rollbackTargetPipelineExecutionId"
        ]
    return out
