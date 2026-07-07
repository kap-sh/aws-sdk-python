"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteIntentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DeleteIntentRequest(TypedDict, closed=True):
    intent_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the intent to delete.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the intent.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot associated with the intent.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntentRequest:
    out: DeleteIntentRequest = {}  # type: ignore[typeddict-item]
    return out
