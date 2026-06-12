"""Generated from Smithy shape ``com.amazonaws.workmail#ListMailboxExportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.jobs
    import aws_sdk_workmail.types.next_token


class ListMailboxExportJobsResponse(TypedDict):
    jobs: NotRequired["aws_sdk_workmail.types.jobs.Jobs"]
    """<p>The mailbox export job details.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMailboxExportJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_workmail.types.jobs

        out["Jobs"] = aws_sdk_workmail.types.jobs.serialize_aws_json_1_1(value["jobs"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMailboxExportJobsResponse:
    out: ListMailboxExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import aws_sdk_workmail.types.jobs

        out["jobs"] = aws_sdk_workmail.types.jobs.deserialize_aws_json_1_1(data["Jobs"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
