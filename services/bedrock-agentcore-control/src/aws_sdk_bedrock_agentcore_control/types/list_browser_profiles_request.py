"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListBrowserProfilesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_name
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListBrowserProfilesRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A token to retrieve the next page of results.</p>"""
    name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.browser_profile_name.BrowserProfileName"
    ]
    """<p>The name of the browser profile to filter results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserProfilesRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ListBrowserProfilesRequest:
    out: ListBrowserProfilesRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
