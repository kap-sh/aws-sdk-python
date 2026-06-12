"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_name_or_arn
    import aws_sdk_sagemaker.types.pipeline_version_id


class DescribePipelineRequest(TypedDict):
    pipeline_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_name_or_arn.PipelineNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the pipeline to describe.</p>"""
    pipeline_version_id: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelineRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelineRequest:
    out: DescribePipelineRequest = {}  # type: ignore[typeddict-item]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineVersionId" in data:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    return out
