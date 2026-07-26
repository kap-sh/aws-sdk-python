"""Generated from Smithy shape ``com.amazonaws.workmail#ListMailboxExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.jobs
    import capo_workmail.types.next_token


class ListMailboxExportJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_workmail.types.jobs.Jobs"]
    """<p>The mailbox export job details.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMailboxExportJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_workmail.types.jobs

        out["Jobs"] = capo_workmail.types.jobs.serialize_aws_json_1_1(value["jobs"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMailboxExportJobsResponse:
    out: ListMailboxExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import capo_workmail.types.jobs

        out["jobs"] = capo_workmail.types.jobs.deserialize_aws_json_1_1(data["Jobs"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
