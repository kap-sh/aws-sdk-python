"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotReplicasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_replica_summary_list
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.replica_region


class ListBotReplicasResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>the unique bot IDs in the list of replicated bots.</p>"""
    source_region: NotRequired["capo_lex_models_v2.types.replica_region.ReplicaRegion"]
    """<p>The source region of the source bots in the list of replicated bots.</p>"""
    bot_replica_summaries: NotRequired[
        "capo_lex_models_v2.types.bot_replica_summary_list.BotReplicaSummaryList"
    ]
    """<p>The summary details for the replicated bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotReplicasResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "bot_replica_summaries" in value:
        import capo_lex_models_v2.types.bot_replica_summary_list

        out["botReplicaSummaries"] = (
            capo_lex_models_v2.types.bot_replica_summary_list.serialize_json(
                value["bot_replica_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBotReplicasResponse:
    out: ListBotReplicasResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "sourceRegion" in data:
        out["source_region"] = data["sourceRegion"]
    if "botReplicaSummaries" in data:
        import capo_lex_models_v2.types.bot_replica_summary_list

        out["bot_replica_summaries"] = (
            capo_lex_models_v2.types.bot_replica_summary_list.deserialize_json(
                data["botReplicaSummaries"]
            )
        )
    return out
