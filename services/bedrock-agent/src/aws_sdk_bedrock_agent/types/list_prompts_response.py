"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListPromptsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.prompt_summaries


class ListPromptsResponse(TypedDict):
    prompt_summaries: "aws_sdk_bedrock_agent.types.prompt_summaries.PromptSummaries"
    """<p>A list, each member of which contains information about a prompt using Prompt management.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.prompt_summaries

    out["promptSummaries"] = (
        aws_sdk_bedrock_agent.types.prompt_summaries.serialize_json(
            value["prompt_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPromptsResponse:
    out: ListPromptsResponse = {}  # type: ignore[typeddict-item]
    if "promptSummaries" in data:
        import aws_sdk_bedrock_agent.types.prompt_summaries

        out["prompt_summaries"] = (
            aws_sdk_bedrock_agent.types.prompt_summaries.deserialize_json(
                data["promptSummaries"]
            )
        )
    else:
        raise DeserializationError("ListPromptsResponse.prompt_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
