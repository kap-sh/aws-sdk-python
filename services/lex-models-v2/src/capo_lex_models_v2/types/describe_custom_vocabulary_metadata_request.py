"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeCustomVocabularyMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class DescribeCustomVocabularyMetadataRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that contains the custom vocabulary.</p>"""
    bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The bot version of the bot to return metadata for.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale to return the custom vocabulary information for. The locale must be <code>en_GB</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomVocabularyMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCustomVocabularyMetadataRequest:
    out: DescribeCustomVocabularyMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
