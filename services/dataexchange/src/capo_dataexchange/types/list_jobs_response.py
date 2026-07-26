"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_job_entry
    import capo_dataexchange.types.next_token


class ListJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_dataexchange.types.list_of_job_entry.ListOfJobEntry"]
    """<p>The jobs listed by the request.</p>"""
    next_token: NotRequired["capo_dataexchange.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_dataexchange.types.list_of_job_entry

        out["Jobs"] = capo_dataexchange.types.list_of_job_entry.serialize_json(
            value["jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import capo_dataexchange.types.list_of_job_entry

        out["jobs"] = capo_dataexchange.types.list_of_job_entry.deserialize_json(
            data["Jobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
