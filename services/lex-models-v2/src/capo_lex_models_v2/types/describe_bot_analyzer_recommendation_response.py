"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotAnalyzerRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_analyzer_recommendation_list
    import capo_lex_models_v2.types.bot_analyzer_status
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.timestamp


class DescribeBotAnalyzerRecommendationResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that was analyzed.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier of the bot locale that was analyzed.</p>"""
    bot_analyzer_status: NotRequired[
        "capo_lex_models_v2.types.bot_analyzer_status.BotAnalyzerStatus"
    ]
    """<p>The current status of the analysis.</p> <p>Valid Values: <code>Processing | Available | Failed | Stopping | Stopped</code> </p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the analysis was initiated.</p>"""
    bot_analyzer_recommendation_list: NotRequired[
        "capo_lex_models_v2.types.bot_analyzer_recommendation_list.BotAnalyzerRecommendationList"
    ]
    """<p>A list of recommendations for optimizing your bot configuration. Each recommendation includes the issue location, priority, description, and proposed fix.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response is truncated, this token can be used in a subsequent request to retrieve the next page of recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotAnalyzerRecommendationResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_analyzer_status" in value:
        import capo_lex_models_v2.types.bot_analyzer_status

        out["botAnalyzerStatus"] = (
            capo_lex_models_v2.types.bot_analyzer_status.serialize_json(
                value["bot_analyzer_status"]
            )
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "bot_analyzer_recommendation_list" in value:
        import capo_lex_models_v2.types.bot_analyzer_recommendation_list

        out["botAnalyzerRecommendationList"] = (
            capo_lex_models_v2.types.bot_analyzer_recommendation_list.serialize_json(
                value["bot_analyzer_recommendation_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeBotAnalyzerRecommendationResponse:
    out: DescribeBotAnalyzerRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botAnalyzerStatus" in data:
        import capo_lex_models_v2.types.bot_analyzer_status

        out["bot_analyzer_status"] = (
            capo_lex_models_v2.types.bot_analyzer_status.deserialize_json(
                data["botAnalyzerStatus"]
            )
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "botAnalyzerRecommendationList" in data:
        import capo_lex_models_v2.types.bot_analyzer_recommendation_list

        out["bot_analyzer_recommendation_list"] = (
            capo_lex_models_v2.types.bot_analyzer_recommendation_list.deserialize_json(
                data["botAnalyzerRecommendationList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
