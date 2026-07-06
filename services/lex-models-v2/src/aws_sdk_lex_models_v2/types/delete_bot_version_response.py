"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_status
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.numerical_bot_version


class DeleteBotVersionResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that is being deleted.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version of the bot that is being deleted.</p>"""
    bot_status: NotRequired["aws_sdk_lex_models_v2.types.bot_status.BotStatus"]
    """<p>The current status of the bot. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotVersionResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_status" in value:
        import aws_sdk_lex_models_v2.types.bot_status

        out["botStatus"] = aws_sdk_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    return out


def deserialize_json(data: dict) -> DeleteBotVersionResponse:
    out: DeleteBotVersionResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_status

        out["bot_status"] = aws_sdk_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    return out
