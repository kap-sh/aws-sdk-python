"""Generated from Smithy shape ``com.amazonaws.macie2#ListClassificationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_job_summary
    import capo_macie2.types.__string


class ListClassificationJobsResponse(TypedDict, closed=True):
    items: NotRequired["capo_macie2.types.__list_of_job_summary.__listOfJobSummary"]
    """<p>An array of objects, one for each job that matches the filter criteria specified in the request.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClassificationJobsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_macie2.types.__list_of_job_summary

        out["items"] = capo_macie2.types.__list_of_job_summary.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClassificationJobsResponse:
    out: ListClassificationJobsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_macie2.types.__list_of_job_summary

        out["items"] = capo_macie2.types.__list_of_job_summary.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
