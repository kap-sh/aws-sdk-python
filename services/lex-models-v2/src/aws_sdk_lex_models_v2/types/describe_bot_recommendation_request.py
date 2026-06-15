"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotRecommendationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DescribeBotRecommendationRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot associated with the bot recommendation.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot associated with the bot recommendation.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    bot_recommendation_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot recommendation to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotRecommendationRequest:
    out: DescribeBotRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out
