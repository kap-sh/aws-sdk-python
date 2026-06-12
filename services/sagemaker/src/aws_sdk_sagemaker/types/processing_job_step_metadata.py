"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingJobStepMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_job_arn


class ProcessingJobStepMetadata(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.processing_job_arn.ProcessingJobArn"]
    """<p>The Amazon Resource Name (ARN) of the processing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingJobStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingJobStepMetadata:
    out: ProcessingJobStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
