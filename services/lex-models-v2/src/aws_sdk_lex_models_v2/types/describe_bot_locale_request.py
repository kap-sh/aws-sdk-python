"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotLocaleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DescribeBotLocaleRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the locale.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot associated with the locale.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotLocaleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotLocaleRequest:
    out: DescribeBotLocaleRequest = {}  # type: ignore[typeddict-item]
    return out
