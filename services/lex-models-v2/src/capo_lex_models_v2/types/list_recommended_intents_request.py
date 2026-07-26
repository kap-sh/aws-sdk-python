"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListRecommendedIntentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token


class ListRecommendedIntentsRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot associated with the recommended intents.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot that contains the recommended intents.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale of the recommended intents.</p>"""
    bot_recommendation_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot recommendation that contains the recommended intents.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListRecommendedIntents operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendedIntentsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListRecommendedIntentsRequest:
    out: ListRecommendedIntentsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
