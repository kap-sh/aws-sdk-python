"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeletePipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_arn


class DeletePipelineResponse(TypedDict):
    pipeline_arn: NotRequired["aws_sdk_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePipelineResponse) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePipelineResponse:
    out: DeletePipelineResponse = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    return out
