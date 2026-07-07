"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasReplicaSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.bot_alias_replication_status
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.failure_reasons
    import aws_sdk_lex_models_v2.types.timestamp


class BotAliasReplicaSummary(TypedDict, closed=True):
    bot_alias_id: NotRequired["aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The bot alias ID for all the alias bot replications.</p>"""
    bot_alias_replication_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_replication_status.BotAliasReplicationStatus"
    ]
    """<p>The replication statuses for all the alias bot replications.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The bot version for all the alias bot replications.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation time and date for all the alias bot replications.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The last time and date updated for all the alias bot replications.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>The reasons for failure for the aliases bot replications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasReplicaSummary) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_alias_replication_status" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_replication_status

        out["botAliasReplicationStatus"] = (
            aws_sdk_lex_models_v2.types.bot_alias_replication_status.serialize_json(
                value["bot_alias_replication_status"]
            )
        )
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
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


def deserialize_json(data: dict) -> BotAliasReplicaSummary:
    out: BotAliasReplicaSummary = {}  # type: ignore[typeddict-item]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botAliasReplicationStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_replication_status

        out["bot_alias_replication_status"] = (
            aws_sdk_lex_models_v2.types.bot_alias_replication_status.deserialize_json(
                data["botAliasReplicationStatus"]
            )
        )
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
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
