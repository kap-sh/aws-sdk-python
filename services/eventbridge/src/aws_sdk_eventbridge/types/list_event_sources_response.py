"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListEventSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_source_list
    import aws_sdk_eventbridge.types.next_token


class ListEventSourcesResponse(TypedDict, closed=True):
    event_sources: NotRequired[
        "aws_sdk_eventbridge.types.event_source_list.EventSourceList"
    ]
    """<p>The list of event sources.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventSourcesResponse) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import aws_sdk_eventbridge.types.event_source_list

        out["EventSources"] = (
            aws_sdk_eventbridge.types.event_source_list.serialize_aws_json_1_1(
                value["event_sources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventSourcesResponse:
    out: ListEventSourcesResponse = {}  # type: ignore[typeddict-item]
    if "EventSources" in data:
        import aws_sdk_eventbridge.types.event_source_list

        out["event_sources"] = (
            aws_sdk_eventbridge.types.event_source_list.deserialize_aws_json_1_1(
                data["EventSources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
