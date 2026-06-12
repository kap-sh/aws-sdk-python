"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerateBotElementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class GenerateBotElementRequest(TypedDict):
    intent_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The intent unique Id for the bot request to generate utterances.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The bot unique Id for the bot request to generate utterances.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The bot version for the bot request to generate utterances.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The unique locale Id for the bot request to generate utterances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateBotElementRequest) -> dict:
    out: dict = {}
    out["intentId"] = value["intent_id"]
    return out


def deserialize_json(data: dict) -> GenerateBotElementRequest:
    out: GenerateBotElementRequest = {}  # type: ignore[typeddict-item]
    if "intentId" in data:
        out["intent_id"] = data["intentId"]
    else:
        raise DeserializationError("GenerateBotElementRequest.intent_id required")
    return out
