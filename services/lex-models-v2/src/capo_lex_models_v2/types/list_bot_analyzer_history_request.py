"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotAnalyzerHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token


class ListBotAnalyzerHistoryRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier to filter the history. If not specified, returns history for all locales.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The bot version to filter the history. If not specified, defaults to <code>DRAFT</code>.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from a previous request was truncated, the <code>nextToken</code> value is used to retrieve the next page of history entries.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of history entries to return in the response. The default is 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotAnalyzerHistoryRequest) -> dict:
    out: dict = {}
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListBotAnalyzerHistoryRequest:
    out: ListBotAnalyzerHistoryRequest = {}  # type: ignore[typeddict-item]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
