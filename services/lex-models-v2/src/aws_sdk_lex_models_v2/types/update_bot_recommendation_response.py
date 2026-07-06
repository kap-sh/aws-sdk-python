"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_recommendation_status
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.encryption_setting
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.timestamp
    import aws_sdk_lex_models_v2.types.transcript_source_setting


class UpdateBotRecommendationResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot containing the bot recommendation that has been updated.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot containing the bot recommendation that has been updated.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    r"""<p>The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> </p>"""
    bot_recommendation_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus"
    ]
    """<p>The status of the bot recommendation.</p> <p>If the status is Failed, then the reasons for the failure are listed in the failureReasons field. </p>"""
    bot_recommendation_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot recommendation to be updated.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot recommendation was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the bot recommendation was last updated.</p>"""
    transcript_source_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.transcript_source_setting.TranscriptSourceSetting"
    ]
    """<p>The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.</p>"""
    encryption_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.encryption_setting.EncryptionSetting"
    ]
    """<p>The object representing the passwords that were used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotRecommendationResponse) -> dict:
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
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    if "transcript_source_setting" in value:
        import aws_sdk_lex_models_v2.types.transcript_source_setting

        out["transcriptSourceSetting"] = (
            aws_sdk_lex_models_v2.types.transcript_source_setting.serialize_json(
                value["transcript_source_setting"]
            )
        )
    if "encryption_setting" in value:
        import aws_sdk_lex_models_v2.types.encryption_setting

        out["encryptionSetting"] = (
            aws_sdk_lex_models_v2.types.encryption_setting.serialize_json(
                value["encryption_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBotRecommendationResponse:
    out: UpdateBotRecommendationResponse = {}  # type: ignore[typeddict-item]
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
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "transcriptSourceSetting" in data:
        import aws_sdk_lex_models_v2.types.transcript_source_setting

        out["transcript_source_setting"] = (
            aws_sdk_lex_models_v2.types.transcript_source_setting.deserialize_json(
                data["transcriptSourceSetting"]
            )
        )
    if "encryptionSetting" in data:
        import aws_sdk_lex_models_v2.types.encryption_setting

        out["encryption_setting"] = (
            aws_sdk_lex_models_v2.types.encryption_setting.deserialize_json(
                data["encryptionSetting"]
            )
        )
    return out
