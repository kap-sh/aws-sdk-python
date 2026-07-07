"""Generated from Smithy shape ``com.amazonaws.location#ListJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.large_token
    import aws_sdk_location.types.list_jobs_response_entry_list


class ListJobsResponse(TypedDict, closed=True):
    entries: (
        "aws_sdk_location.types.list_jobs_response_entry_list.ListJobsResponseEntryList"
    )
    """<p>List of jobs in your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_location.types.large_token.LargeToken"]
    """<p>Token for retrieving the next page (present if more results available).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.list_jobs_response_entry_list

    out["Entries"] = (
        aws_sdk_location.types.list_jobs_response_entry_list.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_location.types.list_jobs_response_entry_list

        out["entries"] = (
            aws_sdk_location.types.list_jobs_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("ListJobsResponse.entries required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
