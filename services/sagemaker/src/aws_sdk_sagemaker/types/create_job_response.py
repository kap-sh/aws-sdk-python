"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_arn


class CreateJobResponse(TypedDict, closed=True):
    job_arn: NotRequired["aws_sdk_sagemaker.types.job_arn.JobArn"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    return out
