"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasHistoryEventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_history_event

BotAliasHistoryEventsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_alias_history_event.BotAliasHistoryEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasHistoryEventsList) -> list:
    import aws_sdk_lex_models_v2.types.bot_alias_history_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.bot_alias_history_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotAliasHistoryEventsList:
    import aws_sdk_lex_models_v2.types.bot_alias_history_event

    out: BotAliasHistoryEventsList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_alias_history_event.deserialize_json(item)
        )
    return out
