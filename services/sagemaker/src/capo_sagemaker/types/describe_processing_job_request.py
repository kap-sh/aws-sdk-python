"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeProcessingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_job_name


class DescribeProcessingJobRequest(TypedDict, closed=True):
    processing_job_name: NotRequired[
        "capo_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProcessingJobRequest) -> dict:
    out: dict = {}
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProcessingJobRequest:
    out: DescribeProcessingJobRequest = {}  # type: ignore[typeddict-item]
    if "ProcessingJobName" in data:
        out["processing_job_name"] = data["ProcessingJobName"]
    return out
