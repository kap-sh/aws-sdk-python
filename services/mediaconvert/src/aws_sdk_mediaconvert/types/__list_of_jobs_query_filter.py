"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfJobsQueryFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.jobs_query_filter

__listOfJobsQueryFilter: TypeAlias = list[
    "aws_sdk_mediaconvert.types.jobs_query_filter.JobsQueryFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobsQueryFilter) -> list:
    import aws_sdk_mediaconvert.types.jobs_query_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.jobs_query_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobsQueryFilter:
    import aws_sdk_mediaconvert.types.jobs_query_filter

    out: __listOfJobsQueryFilter = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.jobs_query_filter.deserialize_json(item))
    return out
