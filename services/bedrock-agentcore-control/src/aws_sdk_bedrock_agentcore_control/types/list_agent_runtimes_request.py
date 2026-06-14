"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentRuntimesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListAgentRuntimesRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRuntimesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentRuntimesRequest:
    out: ListAgentRuntimesRequest = {}  # type: ignore[typeddict-item]
    return out
