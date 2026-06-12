"""Generated from Smithy shape ``com.amazonaws.databrew#ListJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_list
    import aws_sdk_databrew.types.next_token


class ListJobsResponse(TypedDict):
    jobs: "aws_sdk_databrew.types.job_list.JobList"
    """<p>A list of jobs that are defined.</p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.job_list

    out["Jobs"] = aws_sdk_databrew.types.job_list.serialize_json(value["jobs"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import aws_sdk_databrew.types.job_list

        out["jobs"] = aws_sdk_databrew.types.job_list.deserialize_json(data["Jobs"])
    else:
        raise DeserializationError("ListJobsResponse.jobs required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
