"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_recommendation_summary_list
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.next_token


class ListBotRecommendationsResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot that contains the bot recommendation list.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that contains the bot recommendation list.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale of the bot recommendation list.</p>"""
    bot_recommendation_summaries: NotRequired[
        "capo_lex_models_v2.types.bot_recommendation_summary_list.BotRecommendationSummaryList"
    ]
    """<p>Summary information for the bot recommendations that meet the filter specified in this request. The length of the list is specified in the maxResults parameter of the request. If there are more bot recommendations available, the nextToken field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the ListBotRecommendations operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListBotRecommendations operation request to get the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotRecommendationsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_recommendation_summaries" in value:
        import capo_lex_models_v2.types.bot_recommendation_summary_list

        out["botRecommendationSummaries"] = (
            capo_lex_models_v2.types.bot_recommendation_summary_list.serialize_json(
                value["bot_recommendation_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotRecommendationsResponse:
    out: ListBotRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botRecommendationSummaries" in data:
        import capo_lex_models_v2.types.bot_recommendation_summary_list

        out["bot_recommendation_summaries"] = (
            capo_lex_models_v2.types.bot_recommendation_summary_list.deserialize_json(
                data["botRecommendationSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
