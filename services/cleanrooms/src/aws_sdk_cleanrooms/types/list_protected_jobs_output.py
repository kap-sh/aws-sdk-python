"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListProtectedJobsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.protected_job_summary_list


class ListProtectedJobsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    protected_jobs: (
        "aws_sdk_cleanrooms.types.protected_job_summary_list.ProtectedJobSummaryList"
    )
    """<p>A list of protected job summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedJobsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.protected_job_summary_list

    out["protectedJobs"] = (
        aws_sdk_cleanrooms.types.protected_job_summary_list.serialize_json(
            value["protected_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListProtectedJobsOutput:
    out: ListProtectedJobsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "protectedJobs" in data:
        import aws_sdk_cleanrooms.types.protected_job_summary_list

        out["protected_jobs"] = (
            aws_sdk_cleanrooms.types.protected_job_summary_list.deserialize_json(
                data["protectedJobs"]
            )
        )
    else:
        raise DeserializationError("ListProtectedJobsOutput.protected_jobs required")
    return out
