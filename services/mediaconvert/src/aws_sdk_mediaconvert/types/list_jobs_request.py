"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max20
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.job_status
    import aws_sdk_mediaconvert.types.order


class ListJobsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Optional. Number of jobs, up to twenty, that will be returned at one time."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs."""
    order: NotRequired["aws_sdk_mediaconvert.types.order.Order"]
    """Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""
    queue: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. Provide a queue name to get back only jobs from that queue."""
    status: NotRequired["aws_sdk_mediaconvert.types.job_status.JobStatus"]
    """Optional. A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR."""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobsRequest:
    out: ListJobsRequest = {}  # type: ignore[typeddict-item]
    return out
