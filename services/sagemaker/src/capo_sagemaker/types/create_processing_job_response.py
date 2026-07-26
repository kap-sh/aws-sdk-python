"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateProcessingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_job_arn


class CreateProcessingJobResponse(TypedDict, closed=True):
    processing_job_arn: NotRequired[
        "capo_sagemaker.types.processing_job_arn.ProcessingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the processing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProcessingJobResponse) -> dict:
    out: dict = {}
    if "processing_job_arn" in value:
        out["ProcessingJobArn"] = value["processing_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProcessingJobResponse:
    out: CreateProcessingJobResponse = {}  # type: ignore[typeddict-item]
    if "ProcessingJobArn" in data:
        out["processing_job_arn"] = data["ProcessingJobArn"]
    return out
