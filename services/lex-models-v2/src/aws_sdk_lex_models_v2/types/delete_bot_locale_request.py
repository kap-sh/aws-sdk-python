"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotLocaleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DeleteBotLocaleRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that contains the locale.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot that contains the locale. </p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotLocaleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotLocaleRequest:
    out: DeleteBotLocaleRequest = {}  # type: ignore[typeddict-item]
    return out
