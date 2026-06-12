"""Generated from Smithy shape ``com.amazonaws.amplify#ListJobsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.job_summaries
    import aws_sdk_amplify.types.next_token


class ListJobsResult(TypedDict):
    job_summaries: "aws_sdk_amplify.types.job_summaries.JobSummaries"
    """<p>The result structure for the list job result request. </p>"""
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If non-null the pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.job_summaries

    out["jobSummaries"] = aws_sdk_amplify.types.job_summaries.serialize_json(
        value["job_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResult:
    out: ListJobsResult = {}  # type: ignore[typeddict-item]
    if "jobSummaries" in data:
        import aws_sdk_amplify.types.job_summaries

        out["job_summaries"] = aws_sdk_amplify.types.job_summaries.deserialize_json(
            data["jobSummaries"]
        )
    else:
        raise DeserializationError("ListJobsResult.job_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
