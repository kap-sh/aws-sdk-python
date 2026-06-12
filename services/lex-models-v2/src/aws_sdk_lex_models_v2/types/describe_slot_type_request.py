"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeSlotTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DescribeSlotTypeRequest(TypedDict):
    slot_type_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the slot type.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the slot type.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot associated with the slot type.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlotTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSlotTypeRequest:
    out: DescribeSlotTypeRequest = {}  # type: ignore[typeddict-item]
    return out
