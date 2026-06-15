"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListBrowsersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_summaries
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListBrowsersResponse(TypedDict):
    browser_summaries: (
        "aws_sdk_bedrock_agentcore_control.types.browser_summaries.BrowserSummaries"
    )
    """<p>The list of browser summaries.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowsersResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.browser_summaries

    out["browserSummaries"] = (
        aws_sdk_bedrock_agentcore_control.types.browser_summaries.serialize_json(
            value["browser_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowsersResponse:
    out: ListBrowsersResponse = {}  # type: ignore[typeddict-item]
    if "browserSummaries" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_summaries

        out["browser_summaries"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_summaries.deserialize_json(
                data["browserSummaries"]
            )
        )
    else:
        raise DeserializationError("ListBrowsersResponse.browser_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
