"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetJobDetailsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.job_id


class GetJobDetailsInput(TypedDict):
    job_id: "aws_sdk_codepipeline.types.job_id.JobId"
    """<p>The unique system-generated ID for the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobDetailsInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobDetailsInput:
    out: GetJobDetailsInput = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("GetJobDetailsInput.job_id required")
    return out
