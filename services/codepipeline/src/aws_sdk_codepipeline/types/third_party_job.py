"""Generated from Smithy shape ``com.amazonaws.codepipeline#ThirdPartyJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.client_id
    import aws_sdk_codepipeline.types.job_id


class ThirdPartyJob(TypedDict):
    client_id: NotRequired["aws_sdk_codepipeline.types.client_id.ClientId"]
    """<p>The <code>clientToken</code> portion of the <code>clientId</code> and <code>clientToken</code> pair used to verify that the calling entity is allowed access to the job and its details.</p>"""
    job_id: NotRequired["aws_sdk_codepipeline.types.job_id.JobId"]
    """<p>The identifier used to identify the job in CodePipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyJob) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyJob:
    out: ThirdPartyJob = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    return out
