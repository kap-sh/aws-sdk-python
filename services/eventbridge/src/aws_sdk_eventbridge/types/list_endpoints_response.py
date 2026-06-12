"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.endpoint_list
    import aws_sdk_eventbridge.types.next_token


class ListEndpointsResponse(TypedDict):
    endpoints: NotRequired["aws_sdk_eventbridge.types.endpoint_list.EndpointList"]
    """<p>The endpoints returned by the call.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_eventbridge.types.endpoint_list

        out["Endpoints"] = (
            aws_sdk_eventbridge.types.endpoint_list.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsResponse:
    out: ListEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import aws_sdk_eventbridge.types.endpoint_list

        out["endpoints"] = (
            aws_sdk_eventbridge.types.endpoint_list.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
