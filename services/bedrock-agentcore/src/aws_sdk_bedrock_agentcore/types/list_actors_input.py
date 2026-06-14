"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListActorsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.max_results
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.pagination_token


class ListActorsInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource for which to list actors.</p>"""
    max_results: "aws_sdk_bedrock_agentcore.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActorsInput) -> dict:
    out: dict = {}
    out["maxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActorsInput:
    out: ListActorsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
