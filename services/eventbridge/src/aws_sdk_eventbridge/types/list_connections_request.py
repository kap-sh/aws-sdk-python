"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListConnectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connection_name
    import aws_sdk_eventbridge.types.connection_state
    import aws_sdk_eventbridge.types.limit_max100
    import aws_sdk_eventbridge.types.next_token


class ListConnectionsRequest(TypedDict):
    name_prefix: NotRequired["aws_sdk_eventbridge.types.connection_name.ConnectionName"]
    """<p>A name prefix to filter results returned. Only connections with a name that starts with the prefix are returned.</p>"""
    connection_state: NotRequired[
        "aws_sdk_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["aws_sdk_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of connections to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectionsRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "connection_state" in value:
        import aws_sdk_eventbridge.types.connection_state

        out["ConnectionState"] = (
            aws_sdk_eventbridge.types.connection_state.serialize_aws_json_1_1(
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
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "ConnectionState" in data:
        import aws_sdk_eventbridge.types.connection_state

        out["connection_state"] = (
            aws_sdk_eventbridge.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
