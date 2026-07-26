"""Generated from Smithy shape ``com.amazonaws.sagemaker#CacheHitResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_execution_arn


class CacheHitResult(TypedDict, closed=True):
    source_pipeline_execution_arn: NotRequired[
        "capo_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheHitResult) -> dict:
    out: dict = {}
    if "source_pipeline_execution_arn" in value:
        out["SourcePipelineExecutionArn"] = value["source_pipeline_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheHitResult:
    out: CacheHitResult = {}  # type: ignore[typeddict-item]
    if "SourcePipelineExecutionArn" in data:
        out["source_pipeline_execution_arn"] = data["SourcePipelineExecutionArn"]
    return out
