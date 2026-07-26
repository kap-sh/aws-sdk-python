"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_response_list
    import capo_eventbridge.types.next_token


class ListConnectionsResponse(TypedDict, closed=True):
    connections: NotRequired[
        "capo_eventbridge.types.connection_response_list.ConnectionResponseList"
    ]
    """<p>An array of connections objects that include details about the connections.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectionsResponse) -> dict:
    out: dict = {}
    if "connections" in value:
        import capo_eventbridge.types.connection_response_list

        out["Connections"] = (
            capo_eventbridge.types.connection_response_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectionsResponse:
    out: ListConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import capo_eventbridge.types.connection_response_list

        out["connections"] = (
            capo_eventbridge.types.connection_response_list.deserialize_aws_json_1_1(
                data["Connections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
