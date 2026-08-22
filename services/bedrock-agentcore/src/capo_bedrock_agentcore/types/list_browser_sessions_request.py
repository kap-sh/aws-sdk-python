"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListBrowserSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_status
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.next_token


class ListBrowserSessionsRequest(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.</p>"""
    max_results: NotRequired["capo_bedrock_agentcore.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
    ]
    """<p>The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserSessionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "status" in value:
        import capo_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.browser_session_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBrowserSessionsRequest:
    out: ListBrowserSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.browser_session_status.deserialize_json(
                data["status"]
            )
        )
    return out
