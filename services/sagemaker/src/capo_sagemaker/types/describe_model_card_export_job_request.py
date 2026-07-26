"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelCardExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_card_export_job_arn


class DescribeModelCardExportJobRequest(TypedDict, closed=True):
    model_card_export_job_arn: NotRequired[
        "capo_sagemaker.types.model_card_export_job_arn.ModelCardExportJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model card export job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelCardExportJobRequest) -> dict:
    out: dict = {}
    if "model_card_export_job_arn" in value:
        out["ModelCardExportJobArn"] = value["model_card_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelCardExportJobRequest:
    out: DescribeModelCardExportJobRequest = {}  # type: ignore[typeddict-item]
    if "ModelCardExportJobArn" in data:
        out["model_card_export_job_arn"] = data["ModelCardExportJobArn"]
    return out
