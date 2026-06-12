"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogsDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.conversation_logs_data_source_filter_by
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class ConversationLogsDataSource(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The bot Id from the conversation logs.</p>"""
    bot_alias_id: "aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The bot alias Id from the conversation logs.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale Id of the conversation log.</p>"""
    filter: "aws_sdk_lex_models_v2.types.conversation_logs_data_source_filter_by.ConversationLogsDataSourceFilterBy"
    """<p>The filter for the data source of the conversation log.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsDataSource) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botAliasId"] = value["bot_alias_id"]
    out["localeId"] = value["locale_id"]
    import aws_sdk_lex_models_v2.types.conversation_logs_data_source_filter_by

    out["filter"] = (
        aws_sdk_lex_models_v2.types.conversation_logs_data_source_filter_by.serialize_json(
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
        import aws_sdk_lex_models_v2.types.conversation_logs_data_source_filter_by

        out["filter"] = (
            aws_sdk_lex_models_v2.types.conversation_logs_data_source_filter_by.deserialize_json(
                data["filter"]
            )
        )
    else:
        raise DeserializationError("ConversationLogsDataSource.filter required")
    return out
