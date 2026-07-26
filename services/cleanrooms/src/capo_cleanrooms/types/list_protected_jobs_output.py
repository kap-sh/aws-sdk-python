"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListProtectedJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.protected_job_summary_list


class ListProtectedJobsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    protected_jobs: (
        "capo_cleanrooms.types.protected_job_summary_list.ProtectedJobSummaryList"
    )
    """<p>A list of protected job summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedJobsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.protected_job_summary_list

    out["protectedJobs"] = (
        capo_cleanrooms.types.protected_job_summary_list.serialize_json(
            value["protected_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListProtectedJobsOutput:
    out: ListProtectedJobsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "protectedJobs" in data:
        import capo_cleanrooms.types.protected_job_summary_list

        out["protected_jobs"] = (
            capo_cleanrooms.types.protected_job_summary_list.deserialize_json(
                data["protectedJobs"]
            )
        )
    else:
        raise DeserializationError("ListProtectedJobsOutput.protected_jobs required")
    return out
