"""Generated from Smithy shape ``com.amazonaws.connect#LexBotConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.lex_bot
    import aws_sdk_connect.types.lex_v2_bot


class LexBotConfig(TypedDict, closed=True):
    lex_bot: NotRequired["aws_sdk_connect.types.lex_bot.LexBot"]
    lex_v2_bot: NotRequired["aws_sdk_connect.types.lex_v2_bot.LexV2Bot"]
    """<p>Configuration information of an Amazon Lex V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexBotConfig) -> dict:
    out: dict = {}
    if "lex_bot" in value:
        import aws_sdk_connect.types.lex_bot

        out["LexBot"] = aws_sdk_connect.types.lex_bot.serialize_json(value["lex_bot"])
    if "lex_v2_bot" in value:
        import aws_sdk_connect.types.lex_v2_bot

        out["LexV2Bot"] = aws_sdk_connect.types.lex_v2_bot.serialize_json(
            value["lex_v2_bot"]
        )
    return out


def deserialize_json(data: dict) -> LexBotConfig:
    out: LexBotConfig = {}  # type: ignore[typeddict-item]
    if "LexBot" in data:
        import aws_sdk_connect.types.lex_bot

        out["lex_bot"] = aws_sdk_connect.types.lex_bot.deserialize_json(data["LexBot"])
    if "LexV2Bot" in data:
        import aws_sdk_connect.types.lex_v2_bot

        out["lex_v2_bot"] = aws_sdk_connect.types.lex_v2_bot.deserialize_json(
            data["LexV2Bot"]
        )
    return out
