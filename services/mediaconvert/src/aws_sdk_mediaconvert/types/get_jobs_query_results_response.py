"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetJobsQueryResultsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_job
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.jobs_query_status


class GetJobsQueryResultsResponse(TypedDict):
    jobs: NotRequired["aws_sdk_mediaconvert.types.__list_of_job.__listOfJob"]
    """List of jobs."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of jobs via the StartJobsQuery API."""
    status: NotRequired["aws_sdk_mediaconvert.types.jobs_query_status.JobsQueryStatus"]
    """The status of the jobs query."""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobsQueryResultsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_mediaconvert.types.__list_of_job

        out["jobs"] = aws_sdk_mediaconvert.types.__list_of_job.serialize_json(
            value["jobs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "status" in value:
        import aws_sdk_mediaconvert.types.jobs_query_status

        out["status"] = aws_sdk_mediaconvert.types.jobs_query_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetJobsQueryResultsResponse:
    out: GetJobsQueryResultsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_mediaconvert.types.__list_of_job

        out["jobs"] = aws_sdk_mediaconvert.types.__list_of_job.deserialize_json(
            data["jobs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "status" in data:
        import aws_sdk_mediaconvert.types.jobs_query_status

        out["status"] = aws_sdk_mediaconvert.types.jobs_query_status.deserialize_json(
            data["status"]
        )
    return out
