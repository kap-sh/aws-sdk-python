"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotResourceGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bedrock_model_arn
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.generation_input
    import capo_lex_models_v2.types.generation_status
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.presigned_s3_url
    import capo_lex_models_v2.types.timestamp


class DescribeBotResourceGenerationResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot for which the generation request was made.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot for which the generation request was made.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale of the bot for which the generation request was made.</p>"""
    generation_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The generation ID for which to return the generation details.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>A list of reasons why the generation of bot resources through natural language description failed.</p>"""
    generation_status: NotRequired[
        "capo_lex_models_v2.types.generation_status.GenerationStatus"
    ]
    """<p>The status of the generation request.</p>"""
    generation_input_prompt: NotRequired[
        "capo_lex_models_v2.types.generation_input.GenerationInput"
    ]
    """<p>The prompt used in the generation request.</p>"""
    generated_bot_locale_url: NotRequired[
        "capo_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>The Amazon S3 location of the generated bot locale configuration.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the item was generated.</p>"""
    model_arn: NotRequired["capo_lex_models_v2.types.bedrock_model_arn.BedrockModelArn"]
    """<p>The ARN of the model used to generate the bot resources.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the generated item was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotResourceGenerationResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    if "generation_status" in value:
        import capo_lex_models_v2.types.generation_status

        out["generationStatus"] = (
            capo_lex_models_v2.types.generation_status.serialize_json(
                value["generation_status"]
            )
        )
    if "generation_input_prompt" in value:
        out["generationInputPrompt"] = value["generation_input_prompt"]
    if "generated_bot_locale_url" in value:
        out["generatedBotLocaleUrl"] = value["generated_bot_locale_url"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "model_arn" in value:
        out["modelArn"] = value["model_arn"]
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribeBotResourceGenerationResponse:
    out: DescribeBotResourceGenerationResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "generationId" in data:
        out["generation_id"] = data["generationId"]
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "generationStatus" in data:
        import capo_lex_models_v2.types.generation_status

        out["generation_status"] = (
            capo_lex_models_v2.types.generation_status.deserialize_json(
                data["generationStatus"]
            )
        )
    if "generationInputPrompt" in data:
        out["generation_input_prompt"] = data["generationInputPrompt"]
    if "generatedBotLocaleUrl" in data:
        out["generated_bot_locale_url"] = data["generatedBotLocaleUrl"]
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
