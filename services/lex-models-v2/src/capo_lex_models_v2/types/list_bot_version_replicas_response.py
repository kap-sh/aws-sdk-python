"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotVersionReplicasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version_replica_summary_list
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.replica_region


class ListBotVersionReplicasResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique ID of the bots in the list of replicated bots.</p>"""
    source_region: NotRequired["capo_lex_models_v2.types.replica_region.ReplicaRegion"]
    """<p>The source region used for the bots in the list of replicated bots.</p>"""
    replica_region: NotRequired["capo_lex_models_v2.types.replica_region.ReplicaRegion"]
    """<p>The region used for the replicated bots in the list of replicated bots.</p>"""
    bot_version_replica_summaries: NotRequired[
        "capo_lex_models_v2.types.bot_version_replica_summary_list.BotVersionReplicaSummaryList"
    ]
    """<p>The information summary used for the replicated bots in the list of replicated bots.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>The next token used for the replicated bots in the list of replicated bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotVersionReplicasResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "replica_region" in value:
        out["replicaRegion"] = value["replica_region"]
    if "bot_version_replica_summaries" in value:
        import capo_lex_models_v2.types.bot_version_replica_summary_list

        out["botVersionReplicaSummaries"] = (
            capo_lex_models_v2.types.bot_version_replica_summary_list.serialize_json(
                value["bot_version_replica_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotVersionReplicasResponse:
    out: ListBotVersionReplicasResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "sourceRegion" in data:
        out["source_region"] = data["sourceRegion"]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
    if "botVersionReplicaSummaries" in data:
        import capo_lex_models_v2.types.bot_version_replica_summary_list

        out["bot_version_replica_summaries"] = (
            capo_lex_models_v2.types.bot_version_replica_summary_list.deserialize_json(
                data["botVersionReplicaSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
