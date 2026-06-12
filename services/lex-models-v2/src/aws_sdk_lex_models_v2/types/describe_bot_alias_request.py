"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.id


class DescribeBotAliasRequest(TypedDict):
    bot_alias_id: "aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The identifier of the bot alias to describe.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the bot alias to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotAliasRequest:
    out: DescribeBotAliasRequest = {}  # type: ignore[typeddict-item]
    return out
