"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListActorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.actor_summary_list
    import aws_sdk_bedrock_agentcore.types.pagination_token


class ListActorsOutput(TypedDict, closed=True):
    actor_summaries: (
        "aws_sdk_bedrock_agentcore.types.actor_summary_list.ActorSummaryList"
    )
    """<p>The list of actor summaries.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActorsOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.actor_summary_list

    out["actorSummaries"] = (
        aws_sdk_bedrock_agentcore.types.actor_summary_list.serialize_json(
            value["actor_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActorsOutput:
    out: ListActorsOutput = {}  # type: ignore[typeddict-item]
    if "actorSummaries" in data:
        import aws_sdk_bedrock_agentcore.types.actor_summary_list

        out["actor_summaries"] = (
            aws_sdk_bedrock_agentcore.types.actor_summary_list.deserialize_json(
                data["actorSummaries"]
            )
        )
    else:
        raise DeserializationError("ListActorsOutput.actor_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
