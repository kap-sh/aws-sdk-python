"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotExportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id


class BotExportSpecification(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot assigned by Amazon Lex.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot that was exported. This will be either <code>DRAFT</code> or the version number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotExportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    return out


def deserialize_json(data: dict) -> BotExportSpecification:
    out: BotExportSpecification = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("BotExportSpecification.bot_id required")
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError("BotExportSpecification.bot_version required")
    return out
