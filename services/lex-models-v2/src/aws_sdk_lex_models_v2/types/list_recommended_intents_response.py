"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListRecommendedIntentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.recommended_intent_summary_list


class ListRecommendedIntentsResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot associated with the recommended intent.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that contains the intent.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    bot_recommendation_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot recommendation that contains the recommended intent.</p>"""
    summary_list: NotRequired[
        "aws_sdk_lex_models_v2.types.recommended_intent_summary_list.RecommendedIntentSummaryList"
    ]
    """<p>Summary information for the intents that meet the filter criteria specified in the request. The length of the list is specified in the maxResults parameter of the request. If there are more intents available, the nextToken field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the ListRecommendedIntents operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListRecommendedIntents operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendedIntentsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_recommendation_id" in value:
        out["botRecommendationId"] = value["bot_recommendation_id"]
    if "summary_list" in value:
        import aws_sdk_lex_models_v2.types.recommended_intent_summary_list

        out["summaryList"] = (
            aws_sdk_lex_models_v2.types.recommended_intent_summary_list.serialize_json(
                value["summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendedIntentsResponse:
    out: ListRecommendedIntentsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botRecommendationId" in data:
        out["bot_recommendation_id"] = data["botRecommendationId"]
    if "summaryList" in data:
        import aws_sdk_lex_models_v2.types.recommended_intent_summary_list

        out["summary_list"] = (
            aws_sdk_lex_models_v2.types.recommended_intent_summary_list.deserialize_json(
                data["summaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
