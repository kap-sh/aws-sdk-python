"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicaSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.bot_version_replication_status
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.timestamp


class BotVersionReplicaSummary(TypedDict, closed=True):
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The bot version for the summary information for all the version replication statuses.</p>"""
    bot_version_replication_status: NotRequired[
        "capo_lex_models_v2.types.bot_version_replication_status.BotVersionReplicationStatus"
    ]
    """<p>The version replication status for all the replicated bots.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation date and time of the replication status for all the replicated bots.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>The reasons for replication failure for all the replicated bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionReplicaSummary) -> dict:
    out: dict = {}
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_version_replication_status" in value:
        import capo_lex_models_v2.types.bot_version_replication_status

        out["botVersionReplicationStatus"] = (
            capo_lex_models_v2.types.bot_version_replication_status.serialize_json(
                value["bot_version_replication_status"]
            )
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    return out


def deserialize_json(data: dict) -> BotVersionReplicaSummary:
    out: BotVersionReplicaSummary = {}  # type: ignore[typeddict-item]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botVersionReplicationStatus" in data:
        import capo_lex_models_v2.types.bot_version_replication_status

        out["bot_version_replication_status"] = (
            capo_lex_models_v2.types.bot_version_replication_status.deserialize_json(
                data["botVersionReplicationStatus"]
            )
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
