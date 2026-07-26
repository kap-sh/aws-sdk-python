"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotReplicaSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_replica_summary

BotReplicaSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.bot_replica_summary.BotReplicaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotReplicaSummaryList) -> list:
    import capo_lex_models_v2.types.bot_replica_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.bot_replica_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotReplicaSummaryList:
    import capo_lex_models_v2.types.bot_replica_summary

    out: BotReplicaSummaryList = []
    for item in data:
        out.append(capo_lex_models_v2.types.bot_replica_summary.deserialize_json(item))
    return out
