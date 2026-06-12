"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListQueuesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__list_of_queue
    import aws_sdk_mediaconvert.types.__string


class ListQueuesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of queues."""
    queues: NotRequired["aws_sdk_mediaconvert.types.__list_of_queue.__listOfQueue"]
    """List of queues."""
    total_concurrent_jobs: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The maximum number of jobs that MediaConvert can process at one time, across all of your on-demand queues in the current AWS Region."""
    unallocated_concurrent_jobs: NotRequired[
        "aws_sdk_mediaconvert.types.__integer.__integer"
    ]
    """The remaining number of concurrent jobs that are not associated with a queue and are available to allocate to a queue. You can allocate these jobs when you create or update a queue."""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "queues" in value:
        import aws_sdk_mediaconvert.types.__list_of_queue

        out["queues"] = aws_sdk_mediaconvert.types.__list_of_queue.serialize_json(
            value["queues"]
        )
    if "total_concurrent_jobs" in value:
        out["totalConcurrentJobs"] = value["total_concurrent_jobs"]
    if "unallocated_concurrent_jobs" in value:
        out["unallocatedConcurrentJobs"] = value["unallocated_concurrent_jobs"]
    return out


def deserialize_json(data: dict) -> ListQueuesResponse:
    out: ListQueuesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "queues" in data:
        import aws_sdk_mediaconvert.types.__list_of_queue

        out["queues"] = aws_sdk_mediaconvert.types.__list_of_queue.deserialize_json(
            data["queues"]
        )
    if "totalConcurrentJobs" in data:
        out["total_concurrent_jobs"] = data["totalConcurrentJobs"]
    if "unallocatedConcurrentJobs" in data:
        out["unallocated_concurrent_jobs"] = data["unallocatedConcurrentJobs"]
    return out
