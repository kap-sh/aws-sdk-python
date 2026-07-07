"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.numerical_bot_version


class DescribeBotVersionRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot containing the version to return metadata for.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    """<p>The version of the bot to return metadata for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotVersionRequest:
    out: DescribeBotVersionRequest = {}  # type: ignore[typeddict-item]
    return out
