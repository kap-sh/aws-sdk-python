"""Generated from Smithy shape ``com.amazonaws.signer#StartSigningJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.account_id
    import aws_sdk_signer.types.job_id


class StartSigningJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_signer.types.job_id.JobId"]
    """<p>The ID of your signing job.</p>"""
    job_owner: NotRequired["aws_sdk_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the signing job owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSigningJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_owner" in value:
        out["jobOwner"] = value["job_owner"]
    return out


def deserialize_json(data: dict) -> StartSigningJobResponse:
    out: StartSigningJobResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobOwner" in data:
        out["job_owner"] = data["jobOwner"]
    return out
