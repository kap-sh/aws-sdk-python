"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_recommendation_result_statistics
    import aws_sdk_lex_models_v2.types.presigned_s3_url


class BotRecommendationResults(TypedDict, closed=True):
    bot_locale_export_url: NotRequired[
        "aws_sdk_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>The presigned URL link of the recommended bot definition.</p>"""
    associated_transcripts_url: NotRequired[
        "aws_sdk_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>The presigned url link of the associated transcript.</p>"""
    statistics: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_recommendation_result_statistics.BotRecommendationResultStatistics"
    ]
    """<p>The statistical summary of the bot recommendation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotRecommendationResults) -> dict:
    out: dict = {}
    if "bot_locale_export_url" in value:
        out["botLocaleExportUrl"] = value["bot_locale_export_url"]
    if "associated_transcripts_url" in value:
        out["associatedTranscriptsUrl"] = value["associated_transcripts_url"]
    if "statistics" in value:
        import aws_sdk_lex_models_v2.types.bot_recommendation_result_statistics

        out["statistics"] = (
            aws_sdk_lex_models_v2.types.bot_recommendation_result_statistics.serialize_json(
                value["statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> BotRecommendationResults:
    out: BotRecommendationResults = {}  # type: ignore[typeddict-item]
    if "botLocaleExportUrl" in data:
        out["bot_locale_export_url"] = data["botLocaleExportUrl"]
    if "associatedTranscriptsUrl" in data:
        out["associated_transcripts_url"] = data["associatedTranscriptsUrl"]
    if "statistics" in data:
        import aws_sdk_lex_models_v2.types.bot_recommendation_result_statistics

        out["statistics"] = (
            aws_sdk_lex_models_v2.types.bot_recommendation_result_statistics.deserialize_json(
                data["statistics"]
            )
        )
    return out
