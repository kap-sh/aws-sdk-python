"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListHarnessesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListHarnessesRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarnessesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHarnessesRequest:
    out: ListHarnessesRequest = {}  # type: ignore[typeddict-item]
    return out
