"""Generated from Smithy shape ``com.amazonaws.iot#ListJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_summary_list
    import aws_sdk_iot.types.next_token


class ListJobsResponse(TypedDict):
    jobs: NotRequired["aws_sdk_iot.types.job_summary_list.JobSummaryList"]
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_iot.types.job_summary_list

        out["jobs"] = aws_sdk_iot.types.job_summary_list.serialize_json(value["jobs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_iot.types.job_summary_list

        out["jobs"] = aws_sdk_iot.types.job_summary_list.deserialize_json(data["jobs"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
