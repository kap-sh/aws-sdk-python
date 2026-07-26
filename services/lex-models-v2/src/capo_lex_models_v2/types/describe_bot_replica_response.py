"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_replica_status
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.replica_region
    import capo_lex_models_v2.types.timestamp


class DescribeBotReplicaResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique bot ID of the replicated bot being monitored.</p>"""
    replica_region: NotRequired["capo_lex_models_v2.types.replica_region.ReplicaRegion"]
    """<p>The region of the replicated bot being monitored.</p>"""
    source_region: NotRequired["capo_lex_models_v2.types.replica_region.ReplicaRegion"]
    """<p>The source region of the replicated bot being monitored.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation date and time of the replicated bot being monitored.</p>"""
    bot_replica_status: NotRequired[
        "capo_lex_models_v2.types.bot_replica_status.BotReplicaStatus"
    ]
    """<p>The operational status of the replicated bot being monitored.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>The failure reasons the bot being monitored failed to replicate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotReplicaResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "replica_region" in value:
        out["replicaRegion"] = value["replica_region"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "bot_replica_status" in value:
        import capo_lex_models_v2.types.bot_replica_status

        out["botReplicaStatus"] = (
            capo_lex_models_v2.types.bot_replica_status.serialize_json(
                value["bot_replica_status"]
            )
        )
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    return out


def deserialize_json(data: dict) -> DescribeBotReplicaResponse:
    out: DescribeBotReplicaResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
    if "sourceRegion" in data:
        out["source_region"] = data["sourceRegion"]
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "botReplicaStatus" in data:
        import capo_lex_models_v2.types.bot_replica_status

        out["bot_replica_status"] = (
            capo_lex_models_v2.types.bot_replica_status.deserialize_json(
                data["botReplicaStatus"]
            )
        )
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
