"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotAnalyzerHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_analyzer_history_list
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token


class ListBotAnalyzerHistoryResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier used to filter the history.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The bot version used to filter the history.</p>"""
    bot_analyzer_history_list: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_analyzer_history_list.BotAnalyzerHistoryList"
    ]
    """<p>A list of historical analysis executions, ordered by creation date with the most recent first.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response is truncated, this token can be used in a subsequent request to retrieve the next page of history entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotAnalyzerHistoryResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_analyzer_history_list" in value:
        import aws_sdk_lex_models_v2.types.bot_analyzer_history_list

        out["botAnalyzerHistoryList"] = (
            aws_sdk_lex_models_v2.types.bot_analyzer_history_list.serialize_json(
                value["bot_analyzer_history_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotAnalyzerHistoryResponse:
    out: ListBotAnalyzerHistoryResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botAnalyzerHistoryList" in data:
        import aws_sdk_lex_models_v2.types.bot_analyzer_history_list

        out["bot_analyzer_history_list"] = (
            aws_sdk_lex_models_v2.types.bot_analyzer_history_list.deserialize_json(
                data["botAnalyzerHistoryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
