"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePipelineVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_arn
    import aws_sdk_sagemaker.types.pipeline_version_description
    import aws_sdk_sagemaker.types.pipeline_version_id
    import aws_sdk_sagemaker.types.pipeline_version_name


class UpdatePipelineVersionRequest(TypedDict):
    pipeline_arn: NotRequired["aws_sdk_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_version_id: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The pipeline version ID to update.</p>"""
    pipeline_version_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineVersionRequest) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineVersionRequest:
    out: UpdatePipelineVersionRequest = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "PipelineVersionId" in data:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if "PipelineVersionDisplayName" in data:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if "PipelineVersionDescription" in data:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    return out
