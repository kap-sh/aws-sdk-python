"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListBrowsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.resource_type


class ListBrowsersRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.resource_type.ResourceType"
    ]
    """<p>The type of browsers to list. If not specified, all browser types are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBrowsersRequest:
    out: ListBrowsersRequest = {}  # type: ignore[typeddict-item]
    return out
