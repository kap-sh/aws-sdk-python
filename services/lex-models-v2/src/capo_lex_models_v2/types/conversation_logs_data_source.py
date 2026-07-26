"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogsDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.conversation_logs_data_source_filter_by
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class ConversationLogsDataSource(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The bot Id from the conversation logs.</p>"""
    bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The bot alias Id from the conversation logs.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale Id of the conversation log.</p>"""
    filter: "capo_lex_models_v2.types.conversation_logs_data_source_filter_by.ConversationLogsDataSourceFilterBy"
    """<p>The filter for the data source of the conversation log.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsDataSource) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botAliasId"] = value["bot_alias_id"]
    out["localeId"] = value["locale_id"]
    import capo_lex_models_v2.types.conversation_logs_data_source_filter_by

    out["filter"] = (
        capo_lex_models_v2.types.conversation_logs_data_source_filter_by.serialize_json(
            value["filter"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLogsDataSource:
    out: ConversationLogsDataSource = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("ConversationLogsDataSource.bot_id required")
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    else:
        raise DeserializationError("ConversationLogsDataSource.bot_alias_id required")
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError("ConversationLogsDataSource.locale_id required")
    if "filter" in data:
        import capo_lex_models_v2.types.conversation_logs_data_source_filter_by

        out["filter"] = (
            capo_lex_models_v2.types.conversation_logs_data_source_filter_by.deserialize_json(
                data["filter"]
            )
        )
    else:
        raise DeserializationError("ConversationLogsDataSource.filter required")
    return out
