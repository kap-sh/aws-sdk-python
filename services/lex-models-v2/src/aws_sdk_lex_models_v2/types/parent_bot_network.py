"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ParentBotNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id


class ParentBotNetwork(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the network of bots assigned by Amazon Lex.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the network of bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentBotNetwork) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    return out


def deserialize_json(data: dict) -> ParentBotNetwork:
    out: ParentBotNetwork = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("ParentBotNetwork.bot_id required")
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError("ParentBotNetwork.bot_version required")
    return out
