"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListBrowserSessionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_session_summaries
    import aws_sdk_bedrock_agentcore.types.next_token


class ListBrowserSessionsResponse(TypedDict):
    items: "aws_sdk_bedrock_agentcore.types.browser_session_summaries.BrowserSessionSummaries"
    """<p>The list of browser sessions that match the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agentcore.types.next_token.NextToken"]
    """<p>The token to use in a subsequent <code>ListBrowserSessions</code> request to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.browser_session_summaries

    out["items"] = (
        aws_sdk_bedrock_agentcore.types.browser_session_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowserSessionsResponse:
    out: ListBrowserSessionsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bedrock_agentcore.types.browser_session_summaries

        out["items"] = (
            aws_sdk_bedrock_agentcore.types.browser_session_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListBrowserSessionsResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
