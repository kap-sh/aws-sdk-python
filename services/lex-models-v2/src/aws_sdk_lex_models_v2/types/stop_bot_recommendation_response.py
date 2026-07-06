"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StopBotRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_recommendation_status
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class StopBotRecommendationResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot containing the bot recommendation that is being stopped.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot containing the recommendation that is being stopped.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    r"""<p>The identifier of the language and locale of the bot response to stop. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> </p>"""
    bot_recommendation_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus"
    ]
    """<p>The status of the bot recommendation. If the status is Failed, then the reasons for the failure are listed in the failureReasons field.</p>"""
    bot_recommendation_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot recommendation that is being stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBotRecommendationResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_recommendation_status" in value:
        import aws_sdk_lex_models_v2.types.bot_recommendation_status

        out["botRecommendationStatus"] = (
            aws_sdk_lex_models_v2.types.bot_recommendation_status.serialize_json(
                value["bot_recommendation_status"]
            )
        )
    if "bot_recommendation_id" in value:
        out["botRecommendationId"] = value["bot_recommendation_id"]
    return out


def deserialize_json(data: dict) -> StopBotRecommendationResponse:
    out: StopBotRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botRecommendationStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_recommendation_status

        out["bot_recommendation_status"] = (
            aws_sdk_lex_models_v2.types.bot_recommendation_status.deserialize_json(
                data["botRecommendationStatus"]
            )
        )
    if "botRecommendationId" in data:
        out["bot_recommendation_id"] = data["botRecommendationId"]
    return out
