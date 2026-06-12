"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListPrefetchSchedulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer_min1_max100
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.list_prefetch_schedule_type


class ListPrefetchSchedulesRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_mediatailor.types.__integer_min1_max100.__integerMin1Max100"
    ]
    """<p>The maximum number of prefetch schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> prefetch schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListPrefetchSchedules</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>"""
    playback_configuration_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>Retrieves the prefetch schedule(s) for a specific playback configuration.</p>"""
    schedule_type: NotRequired[
        "aws_sdk_mediatailor.types.list_prefetch_schedule_type.ListPrefetchScheduleType"
    ]
    """<p>The type of prefetch schedules that you want to list. <code>SINGLE</code> indicates that you want to list the configured single prefetch schedules. <code>RECURRING</code> indicates that you want to list the configured recurring prefetch schedules. <code>ALL</code> indicates that you want to list all configured prefetch schedules.</p>"""
    stream_id: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrefetchSchedulesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "schedule_type" in value:
        import aws_sdk_mediatailor.types.list_prefetch_schedule_type

        out["ScheduleType"] = (
            aws_sdk_mediatailor.types.list_prefetch_schedule_type.serialize_json(
                value["schedule_type"]
            )
        )
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_json(data: dict) -> ListPrefetchSchedulesRequest:
    out: ListPrefetchSchedulesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ScheduleType" in data:
        import aws_sdk_mediatailor.types.list_prefetch_schedule_type

        out["schedule_type"] = (
            aws_sdk_mediatailor.types.list_prefetch_schedule_type.deserialize_json(
                data["ScheduleType"]
            )
        )
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
