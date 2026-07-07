"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_replica_status
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.replica_region


class DeleteBotReplicaResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique bot ID of the replicated bot generated.</p>"""
    replica_region: NotRequired[
        "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    ]
    """<p>The region of the replicated bot generated.</p>"""
    bot_replica_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_replica_status.BotReplicaStatus"
    ]
    """<p>The operational status of the replicated bot generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotReplicaResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "replica_region" in value:
        out["replicaRegion"] = value["replica_region"]
    if "bot_replica_status" in value:
        import aws_sdk_lex_models_v2.types.bot_replica_status

        out["botReplicaStatus"] = (
            aws_sdk_lex_models_v2.types.bot_replica_status.serialize_json(
                value["bot_replica_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteBotReplicaResponse:
    out: DeleteBotReplicaResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
    if "botReplicaStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_replica_status

        out["bot_replica_status"] = (
            aws_sdk_lex_models_v2.types.bot_replica_status.deserialize_json(
                data["botReplicaStatus"]
            )
        )
    return out
