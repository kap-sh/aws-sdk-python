"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartBotRecommendationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.encryption_setting
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.transcript_source_setting


class StartBotRecommendationRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot containing the bot recommendation.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot containing the bot recommendation.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> </p>"""
    transcript_source_setting: (
        "aws_sdk_lex_models_v2.types.transcript_source_setting.TranscriptSourceSetting"
    )
    """<p>The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.</p>"""
    encryption_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.encryption_setting.EncryptionSetting"
    ]
    """<p>The object representing the passwords that will be used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBotRecommendationRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> StartBotRecommendationRequest:
    out: StartBotRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "transcriptSourceSetting" in data:
        import aws_sdk_lex_models_v2.types.transcript_source_setting

        out["transcript_source_setting"] = (
            aws_sdk_lex_models_v2.types.transcript_source_setting.deserialize_json(
                data["transcriptSourceSetting"]
            )
        )
    else:
        raise DeserializationError(
            "StartBotRecommendationRequest.transcript_source_setting required"
        )
    if "encryptionSetting" in data:
        import aws_sdk_lex_models_v2.types.encryption_setting

        out["encryption_setting"] = (
            aws_sdk_lex_models_v2.types.encryption_setting.deserialize_json(
                data["encryptionSetting"]
            )
        )
    return out
