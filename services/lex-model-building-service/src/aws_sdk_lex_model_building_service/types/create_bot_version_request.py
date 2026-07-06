"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CreateBotVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.string


class CreateBotVersionRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot that you want to create a new version of. The name is case sensitive. </p>"""
    checksum: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>Identifies a specific revision of the <code>$LATEST</code> version of the bot. If you specify a checksum and the <code>$LATEST</code> version of the bot has a different checksum, a <code>PreconditionFailedException</code> exception is returned and Amazon Lex doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the <code>$LATEST</code> version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotVersionRequest) -> dict:
    out: dict = {}
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    return out


def deserialize_json(data: dict) -> CreateBotVersionRequest:
    out: CreateBotVersionRequest = {}  # type: ignore[typeddict-item]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    return out
