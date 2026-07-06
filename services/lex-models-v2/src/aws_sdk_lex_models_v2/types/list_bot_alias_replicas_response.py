"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotAliasReplicasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_replica_summary_list
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.replica_region


class ListBotAliasReplicasResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique bot ID of the replicated bot created from the source bot alias.</p>"""
    source_region: NotRequired[
        "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    ]
    """<p>The source region of the replicated bot created from the source bot alias.</p>"""
    replica_region: NotRequired[
        "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    ]
    """<p>The secondary region of the replicated bot created from the source bot alias.</p>"""
    bot_alias_replica_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_replica_summary_list.BotAliasReplicaSummaryList"
    ]
    """<p>The summary information of the replicated bot created from the source bot alias.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>The next token for the replicated bots created from the source bot alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotAliasReplicasResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "replica_region" in value:
        out["replicaRegion"] = value["replica_region"]
    if "bot_alias_replica_summaries" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_replica_summary_list

        out["botAliasReplicaSummaries"] = (
            aws_sdk_lex_models_v2.types.bot_alias_replica_summary_list.serialize_json(
                value["bot_alias_replica_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotAliasReplicasResponse:
    out: ListBotAliasReplicasResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "sourceRegion" in data:
        out["source_region"] = data["sourceRegion"]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
    if "botAliasReplicaSummaries" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_replica_summary_list

        out["bot_alias_replica_summaries"] = (
            aws_sdk_lex_models_v2.types.bot_alias_replica_summary_list.deserialize_json(
                data["botAliasReplicaSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
