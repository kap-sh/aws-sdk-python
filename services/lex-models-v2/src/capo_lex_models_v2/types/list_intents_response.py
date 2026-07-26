"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.intent_summary_list
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.next_token


class ListIntentsResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the intent.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot that contains the intent.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale of the intents in the list.</p>"""
    intent_summaries: NotRequired[
        "capo_lex_models_v2.types.intent_summary_list.IntentSummaryList"
    ]
    """<p>Summary information for the intents that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more intents available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListIntents</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListIntents</code> operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntentsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "intent_summaries" in value:
        import capo_lex_models_v2.types.intent_summary_list

        out["intentSummaries"] = (
            capo_lex_models_v2.types.intent_summary_list.serialize_json(
                value["intent_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntentsResponse:
    out: ListIntentsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "intentSummaries" in data:
        import capo_lex_models_v2.types.intent_summary_list

        out["intent_summaries"] = (
            capo_lex_models_v2.types.intent_summary_list.deserialize_json(
                data["intentSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
