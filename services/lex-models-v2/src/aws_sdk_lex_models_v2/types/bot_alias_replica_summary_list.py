"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasReplicaSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_replica_summary

BotAliasReplicaSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_alias_replica_summary.BotAliasReplicaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasReplicaSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.bot_alias_replica_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.bot_alias_replica_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotAliasReplicaSummaryList:
    import aws_sdk_lex_models_v2.types.bot_alias_replica_summary

    out: BotAliasReplicaSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_alias_replica_summary.deserialize_json(item)
        )
    return out
