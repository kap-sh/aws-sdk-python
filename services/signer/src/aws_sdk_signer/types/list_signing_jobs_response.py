"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.next_token
    import aws_sdk_signer.types.signing_jobs


class ListSigningJobsResponse(TypedDict):
    jobs: NotRequired["aws_sdk_signer.types.signing_jobs.SigningJobs"]
    """<p>A list of your signing jobs.</p>"""
    next_token: NotRequired["aws_sdk_signer.types.next_token.NextToken"]
    """<p>String for specifying the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSigningJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_signer.types.signing_jobs

        out["jobs"] = aws_sdk_signer.types.signing_jobs.serialize_json(value["jobs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSigningJobsResponse:
    out: ListSigningJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_signer.types.signing_jobs

        out["jobs"] = aws_sdk_signer.types.signing_jobs.deserialize_json(data["jobs"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
