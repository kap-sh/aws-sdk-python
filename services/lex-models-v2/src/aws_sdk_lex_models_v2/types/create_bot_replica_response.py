"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotReplicaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_replica_status
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.replica_region
    import aws_sdk_lex_models_v2.types.timestamp


class CreateBotReplicaResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique bot ID of the replicated bot generated.</p>"""
    replica_region: NotRequired[
        "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    ]
    """<p>The region of the replicated bot generated.</p>"""
    source_region: NotRequired[
        "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    ]
    """<p>The source region for the source bot used for the replicated bot generated.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation date and time of the replicated bot generated.</p>"""
    bot_replica_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_replica_status.BotReplicaStatus"
    ]
    """<p>The operational status of the replicated bot generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotReplicaResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "replica_region" in value:
        out["replicaRegion"] = value["replica_region"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "bot_replica_status" in value:
        import aws_sdk_lex_models_v2.types.bot_replica_status

        out["botReplicaStatus"] = (
            aws_sdk_lex_models_v2.types.bot_replica_status.serialize_json(
                value["bot_replica_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBotReplicaResponse:
    out: CreateBotReplicaResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
    if "sourceRegion" in data:
        out["source_region"] = data["sourceRegion"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "botReplicaStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_replica_status

        out["bot_replica_status"] = (
            aws_sdk_lex_models_v2.types.bot_replica_status.deserialize_json(
                data["botReplicaStatus"]
            )
        )
    return out
