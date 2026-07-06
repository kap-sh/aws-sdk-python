"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServiceEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.service_event_type_list


class ListServiceEventsRequest(TypedDict, closed=True):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    event_types: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_event_type_list.ServiceEventTypeList"
    ]
    """<p>Filter events by type.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time for filtering events.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for filtering events.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceEventsRequest:
    out: ListServiceEventsRequest = {}  # type: ignore[typeddict-item]
    return out
