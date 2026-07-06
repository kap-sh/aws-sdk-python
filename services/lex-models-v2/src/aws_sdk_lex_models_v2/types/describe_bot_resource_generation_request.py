"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotResourceGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DescribeBotResourceGenerationRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot for which to return the generation details.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot for which to return the generation details.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale of the bot for which to return the generation details.</p>"""
    generation_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the generation request for which to return the generation details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotResourceGenerationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotResourceGenerationRequest:
    out: DescribeBotResourceGenerationRequest = {}  # type: ignore[typeddict-item]
    return out
