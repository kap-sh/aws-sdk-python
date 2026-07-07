"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListPromptsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.prompt_identifier


class ListPromptsRequest(TypedDict, closed=True):
    prompt_identifier: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
    ]
    """<p>The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.</p>"""
    max_results: NotRequired["aws_sdk_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPromptsRequest:
    out: ListPromptsRequest = {}  # type: ignore[typeddict-item]
    return out
