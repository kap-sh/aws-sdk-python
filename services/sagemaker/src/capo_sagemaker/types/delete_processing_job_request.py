"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteProcessingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_job_name


class DeleteProcessingJobRequest(TypedDict, closed=True):
    processing_job_name: NotRequired[
        "capo_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the processing job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProcessingJobRequest) -> dict:
    out: dict = {}
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProcessingJobRequest:
    out: DeleteProcessingJobRequest = {}  # type: ignore[typeddict-item]
    if "ProcessingJobName" in data:
        out["processing_job_name"] = data["ProcessingJobName"]
    return out
