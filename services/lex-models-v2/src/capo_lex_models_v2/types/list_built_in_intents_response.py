"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBuiltInIntentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.built_in_intent_summary_list
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.next_token


class ListBuiltInIntentsResponse(TypedDict, closed=True):
    built_in_intent_summaries: NotRequired[
        "capo_lex_models_v2.types.built_in_intent_summary_list.BuiltInIntentSummaryList"
    ]
    """<p>Summary information for the built-in intents that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more intents available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBuiltInIntents</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListBotAliases</code> operation request to get the next page of results.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale of the intents in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBuiltInIntentsResponse) -> dict:
    out: dict = {}
    if "built_in_intent_summaries" in value:
        import capo_lex_models_v2.types.built_in_intent_summary_list

        out["builtInIntentSummaries"] = (
            capo_lex_models_v2.types.built_in_intent_summary_list.serialize_json(
                value["built_in_intent_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> ListBuiltInIntentsResponse:
    out: ListBuiltInIntentsResponse = {}  # type: ignore[typeddict-item]
    if "builtInIntentSummaries" in data:
        import capo_lex_models_v2.types.built_in_intent_summary_list

        out["built_in_intent_summaries"] = (
            capo_lex_models_v2.types.built_in_intent_summary_list.deserialize_json(
                data["builtInIntentSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    return out
