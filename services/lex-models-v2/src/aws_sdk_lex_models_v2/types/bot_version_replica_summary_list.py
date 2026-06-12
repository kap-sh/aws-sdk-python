"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicaSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version_replica_summary

BotVersionReplicaSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_version_replica_summary.BotVersionReplicaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionReplicaSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.bot_version_replica_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.bot_version_replica_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotVersionReplicaSummaryList:
    import aws_sdk_lex_models_v2.types.bot_version_replica_summary

    out: BotVersionReplicaSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_version_replica_summary.deserialize_json(
                item
            )
        )
    return out
