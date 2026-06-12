"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotReplicaSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_replica_status
    import aws_sdk_lex_models_v2.types.failure_reasons
    import aws_sdk_lex_models_v2.types.replica_region
    import aws_sdk_lex_models_v2.types.timestamp


class BotReplicaSummary(TypedDict):
    replica_region: NotRequired[
        "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    ]
    """<p>The replica region used in the replication statuses summary.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation time and date for the replicated bots.</p>"""
    bot_replica_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_replica_status.BotReplicaStatus"
    ]
    """<p>The operation status for the replicated bot applicable.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>The reasons for the failure for the replicated bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotReplicaSummary) -> dict:
    out: dict = {}
    if "replica_region" in value:
        out["replicaRegion"] = value["replica_region"]
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
    if "failure_reasons" in value:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> BotReplicaSummary:
    out: BotReplicaSummary = {}  # type: ignore[typeddict-item]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
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
    if "failureReasons" in data:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
