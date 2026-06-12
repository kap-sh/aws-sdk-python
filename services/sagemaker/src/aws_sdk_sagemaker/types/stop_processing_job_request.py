"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopProcessingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_job_name


class StopProcessingJobRequest(TypedDict):
    processing_job_name: NotRequired[
        "aws_sdk_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the processing job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopProcessingJobRequest) -> dict:
    out: dict = {}
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopProcessingJobRequest:
    out: StopProcessingJobRequest = {}  # type: ignore[typeddict-item]
    if "ProcessingJobName" in data:
        out["processing_job_name"] = data["ProcessingJobName"]
    return out
