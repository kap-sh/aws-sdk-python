"""Generated from Smithy shape ``com.amazonaws.codepipeline#AcknowledgeJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.job_id
    import aws_sdk_codepipeline.types.nonce


class AcknowledgeJobInput(TypedDict, closed=True):
    job_id: "aws_sdk_codepipeline.types.job_id.JobId"
    """<p>The unique system-generated ID of the job for which you want to confirm receipt.</p>"""
    nonce: "aws_sdk_codepipeline.types.nonce.Nonce"
    """<p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the <a>PollForJobs</a> request that returned this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeJobInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["nonce"] = value["nonce"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeJobInput:
    out: AcknowledgeJobInput = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("AcknowledgeJobInput.job_id required")
    if "nonce" in data:
        out["nonce"] = data["nonce"]
    else:
        raise DeserializationError("AcknowledgeJobInput.nonce required")
    return out
