"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListSessionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.actor_id
    import aws_sdk_bedrock_agentcore.types.max_results
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.pagination_token
    import aws_sdk_bedrock_agentcore.types.session_filter


class ListSessionsInput(TypedDict, closed=True):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource for which to list sessions.</p>"""
    actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor for which to list sessions. </p>"""
    max_results: "aws_sdk_bedrock_agentcore.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    filter: NotRequired["aws_sdk_bedrock_agentcore.types.session_filter.SessionFilter"]
    """<p>Filter criteria to apply when listing sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsInput) -> dict:
    out: dict = {}
    out["maxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filter" in value:
        import aws_sdk_bedrock_agentcore.types.session_filter

        out["filter"] = aws_sdk_bedrock_agentcore.types.session_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListSessionsInput:
    out: ListSessionsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filter" in data:
        import aws_sdk_bedrock_agentcore.types.session_filter

        out["filter"] = aws_sdk_bedrock_agentcore.types.session_filter.deserialize_json(
            data["filter"]
        )
    return out
