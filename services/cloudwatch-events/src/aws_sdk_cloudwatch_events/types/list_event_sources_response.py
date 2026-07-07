"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListEventSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_source_list
    import aws_sdk_cloudwatch_events.types.next_token


class ListEventSourcesResponse(TypedDict, closed=True):
    event_sources: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_source_list.EventSourceList"
    ]
    """<p>The list of event sources.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>A token you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventSourcesResponse) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import aws_sdk_cloudwatch_events.types.event_source_list

        out["EventSources"] = (
            aws_sdk_cloudwatch_events.types.event_source_list.serialize_aws_json_1_1(
                value["event_sources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventSourcesResponse:
    out: ListEventSourcesResponse = {}  # type: ignore[typeddict-item]
    if "EventSources" in data:
        import aws_sdk_cloudwatch_events.types.event_source_list

        out["event_sources"] = (
            aws_sdk_cloudwatch_events.types.event_source_list.deserialize_aws_json_1_1(
                data["EventSources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
