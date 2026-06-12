"""Generated from Smithy shape ``com.amazonaws.apprunner#ListConnectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.connection_name
    import aws_sdk_apprunner.types.max_results
    import aws_sdk_apprunner.types.next_token


class ListConnectionsRequest(TypedDict):
    connection_name: NotRequired[
        "aws_sdk_apprunner.types.connection_name.ConnectionName"
    ]
    """<p>If specified, only this connection is returned. If not specified, the result isn't filtered by name.</p>"""
    max_results: NotRequired["aws_sdk_apprunner.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in each response (result page). Used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>A token from a previous result page. Used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsRequest) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsRequest:
    out: ListConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
