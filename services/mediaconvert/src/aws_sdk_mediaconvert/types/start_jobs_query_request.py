"""Generated from Smithy shape ``com.amazonaws.mediaconvert#StartJobsQueryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max20
    import aws_sdk_mediaconvert.types.__list_of_jobs_query_filter
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.order


class StartJobsQueryRequest(TypedDict):
    filter_list: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_jobs_query_filter.__listOfJobsQueryFilter"
    ]
    """Optional. Provide an array of JobsQueryFilters for your StartJobsQuery request."""
    max_results: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Optional. Number of jobs, up to twenty, that will be included in the jobs query."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of jobs matched by a jobs query."""
    order: NotRequired["aws_sdk_mediaconvert.types.order.Order"]
    """Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobsQueryRequest) -> dict:
    out: dict = {}
    if "filter_list" in value:
        import aws_sdk_mediaconvert.types.__list_of_jobs_query_filter

        out["filterList"] = (
            aws_sdk_mediaconvert.types.__list_of_jobs_query_filter.serialize_json(
                value["filter_list"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "order" in value:
        import aws_sdk_mediaconvert.types.order

        out["order"] = aws_sdk_mediaconvert.types.order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> StartJobsQueryRequest:
    out: StartJobsQueryRequest = {}  # type: ignore[typeddict-item]
    if "filterList" in data:
        import aws_sdk_mediaconvert.types.__list_of_jobs_query_filter

        out["filter_list"] = (
            aws_sdk_mediaconvert.types.__list_of_jobs_query_filter.deserialize_json(
                data["filterList"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "order" in data:
        import aws_sdk_mediaconvert.types.order

        out["order"] = aws_sdk_mediaconvert.types.order.deserialize_json(data["order"])
    return out
