"""Generated from Smithy shape ``com.amazonaws.connect#LexBot``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.bot_name
    import aws_sdk_connect.types.lex_region


class LexBot(TypedDict, closed=True):
    name: "aws_sdk_connect.types.bot_name.BotName"
    """<p>The name of the Amazon Lex bot.</p>"""
    lex_region: "aws_sdk_connect.types.lex_region.LexRegion"
    """<p>The Amazon Web Services Region where the Amazon Lex bot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexBot) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["LexRegion"] = value["lex_region"]
    return out


def deserialize_json(data: dict) -> LexBot:
    out: LexBot = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("LexBot.name required")
    if "LexRegion" in data:
        out["lex_region"] = data["LexRegion"]
    else:
        raise DeserializationError("LexBot.lex_region required")
    return out
