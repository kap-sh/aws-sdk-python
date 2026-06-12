"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleHistoryEventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_history_event

BotLocaleHistoryEventsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_locale_history_event.BotLocaleHistoryEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleHistoryEventsList) -> list:
    import aws_sdk_lex_models_v2.types.bot_locale_history_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.bot_locale_history_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotLocaleHistoryEventsList:
    import aws_sdk_lex_models_v2.types.bot_locale_history_event

    out: BotLocaleHistoryEventsList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_locale_history_event.deserialize_json(item)
        )
    return out
