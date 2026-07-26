"""Generated from Smithy shape ``com.amazonaws.sesv2#ListExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.export_job_summary_list
    import capo_sesv2.types.next_token


class ListExportJobsResponse(TypedDict, closed=True):
    export_jobs: NotRequired[
        "capo_sesv2.types.export_job_summary_list.ExportJobSummaryList"
    ]
    """<p>A list of the export job summaries.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional export jobs available to be listed. Use this token to a subsequent call to <code>ListExportJobs</code> with the same parameters to retrieve the next page of export jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportJobsResponse) -> dict:
    out: dict = {}
    if "export_jobs" in value:
        import capo_sesv2.types.export_job_summary_list

        out["ExportJobs"] = capo_sesv2.types.export_job_summary_list.serialize_json(
            value["export_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportJobsResponse:
    out: ListExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ExportJobs" in data:
        import capo_sesv2.types.export_job_summary_list

        out["export_jobs"] = capo_sesv2.types.export_job_summary_list.deserialize_json(
            data["ExportJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
