"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListSyncJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.sync_job_summaries


class ListSyncJobsResponse(TypedDict, closed=True):
    sync_job_summaries: NotRequired[
        "aws_sdk_iottwinmaker.types.sync_job_summaries.SyncJobSummaries"
    ]
    """<p>The listed SyncJob summaries.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSyncJobsResponse) -> dict:
    out: dict = {}
    if "sync_job_summaries" in value:
        import aws_sdk_iottwinmaker.types.sync_job_summaries

        out["syncJobSummaries"] = (
            aws_sdk_iottwinmaker.types.sync_job_summaries.serialize_json(
                value["sync_job_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSyncJobsResponse:
    out: ListSyncJobsResponse = {}  # type: ignore[typeddict-item]
    if "syncJobSummaries" in data:
        import aws_sdk_iottwinmaker.types.sync_job_summaries

        out["sync_job_summaries"] = (
            aws_sdk_iottwinmaker.types.sync_job_summaries.deserialize_json(
                data["syncJobSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
