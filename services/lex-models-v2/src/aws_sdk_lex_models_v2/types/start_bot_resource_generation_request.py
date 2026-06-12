"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartBotResourceGenerationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.generation_input
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class StartBotResourceGenerationRequest(TypedDict):
    generation_input_prompt: (
        "aws_sdk_lex_models_v2.types.generation_input.GenerationInput"
    )
    """<p>The prompt to generate intents and slot types for the bot locale. Your description should be both <i>detailed</i> and <i>precise</i> to help generate appropriate and sufficient intents for your bot. Include a list of actions to improve the intent creation process.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot for which to generate intents and slot types.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot for which to generate intents and slot types.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale of the bot for which to generate intents and slot types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBotResourceGenerationRequest) -> dict:
    out: dict = {}
    out["generationInputPrompt"] = value["generation_input_prompt"]
    return out


def deserialize_json(data: dict) -> StartBotResourceGenerationRequest:
    out: StartBotResourceGenerationRequest = {}  # type: ignore[typeddict-item]
    if "generationInputPrompt" in data:
        out["generation_input_prompt"] = data["generationInputPrompt"]
    else:
        raise DeserializationError(
            "StartBotResourceGenerationRequest.generation_input_prompt required"
        )
    return out
