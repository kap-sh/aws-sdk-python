"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecuteQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.execute_query_max_results
    import aws_sdk_iotsitewise.types.execute_query_next_token
    import aws_sdk_iotsitewise.types.query_statement


class ExecuteQueryRequest(TypedDict, closed=True):
    query_statement: "aws_sdk_iotsitewise.types.query_statement.QueryStatement"
    """<p>The IoT SiteWise query statement.</p>"""
    next_token: NotRequired[
        "aws_sdk_iotsitewise.types.execute_query_next_token.ExecuteQueryNextToken"
    ]
    """<p>The string that specifies the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iotsitewise.types.execute_query_max_results.ExecuteQueryMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p> <ul> <li> <p>Minimum is 1</p> </li> <li> <p>Maximum is 20000</p> </li> <li> <p>Default is 20000</p> </li> </ul>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteQueryRequest) -> dict:
    out: dict = {}
    out["queryStatement"] = value["query_statement"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ExecuteQueryRequest:
    out: ExecuteQueryRequest = {}  # type: ignore[typeddict-item]
    if "queryStatement" in data:
        out["query_statement"] = data["queryStatement"]
    else:
        raise DeserializationError("ExecuteQueryRequest.query_statement required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
