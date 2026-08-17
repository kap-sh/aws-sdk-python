"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListEventSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_source_list
    import capo_eventbridge.types.next_token


class ListEventSourcesResponse(TypedDict, closed=True):
    event_sources: NotRequired[
        "capo_eventbridge.types.event_source_list.EventSourceList"
    ]
    """<p>The list of event sources.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventSourcesResponse) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import capo_eventbridge.types.event_source_list

        out["EventSources"] = (
            capo_eventbridge.types.event_source_list.serialize_aws_json_1_1(
                value["event_sources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventSourcesResponse:
    out: ListEventSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventSources") is not None:
        import capo_eventbridge.types.event_source_list

        out["event_sources"] = (
            capo_eventbridge.types.event_source_list.deserialize_aws_json_1_1(
                data["EventSources"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
