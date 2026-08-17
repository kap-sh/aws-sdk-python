"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_name
    import capo_eventbridge.types.connection_state
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token


class ListConnectionsRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_eventbridge.types.connection_name.ConnectionName"]
    """<p>A name prefix to filter results returned. Only connections with a name that starts with the prefix are returned.</p>"""
    connection_state: NotRequired[
        "capo_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of connections to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectionsRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "connection_state" in value:
        import capo_eventbridge.types.connection_state

        out["ConnectionState"] = (
            capo_eventbridge.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectionsRequest:
    out: ListConnectionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    if data.get("ConnectionState") is not None:
        import capo_eventbridge.types.connection_state

        out["connection_state"] = (
            capo_eventbridge.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
