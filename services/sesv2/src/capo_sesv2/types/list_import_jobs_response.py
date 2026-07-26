"""Generated from Smithy shape ``com.amazonaws.sesv2#ListImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.import_job_summary_list
    import capo_sesv2.types.next_token


class ListImportJobsResponse(TypedDict, closed=True):
    import_jobs: NotRequired[
        "capo_sesv2.types.import_job_summary_list.ImportJobSummaryList"
    ]
    """<p>A list of the import job summaries.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to <code>ListImportJobs</code> with the same parameters to retrieve the next page of import jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportJobsResponse) -> dict:
    out: dict = {}
    if "import_jobs" in value:
        import capo_sesv2.types.import_job_summary_list

        out["ImportJobs"] = capo_sesv2.types.import_job_summary_list.serialize_json(
            value["import_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportJobsResponse:
    out: ListImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobs" in data:
        import capo_sesv2.types.import_job_summary_list

        out["import_jobs"] = capo_sesv2.types.import_job_summary_list.deserialize_json(
            data["ImportJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
