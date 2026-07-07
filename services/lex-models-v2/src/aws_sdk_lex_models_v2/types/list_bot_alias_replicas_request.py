"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotAliasReplicasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.replica_region


class ListBotAliasReplicasRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The request for the unique bot ID of the replicated bot created from the source bot alias.</p>"""
    replica_region: "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the secondary region of the replicated bot created from the source bot alias.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The request for maximum results to list the replicated bots created from the source bot alias.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>The request for the next token for the replicated bot created from the source bot alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotAliasReplicasRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotAliasReplicasRequest:
    out: ListBotAliasReplicasRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
