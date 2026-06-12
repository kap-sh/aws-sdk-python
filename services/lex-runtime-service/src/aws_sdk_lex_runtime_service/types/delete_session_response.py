"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DeleteSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.bot_alias
    import aws_sdk_lex_runtime_service.types.bot_name
    import aws_sdk_lex_runtime_service.types.string
    import aws_sdk_lex_runtime_service.types.user_id


class DeleteSessionResponse(TypedDict):
    bot_name: NotRequired["aws_sdk_lex_runtime_service.types.bot_name.BotName"]
    """<p>The name of the bot associated with the session data.</p>"""
    bot_alias: NotRequired["aws_sdk_lex_runtime_service.types.bot_alias.BotAlias"]
    """<p>The alias in use for the bot associated with the session data.</p>"""
    user_id: NotRequired["aws_sdk_lex_runtime_service.types.user_id.UserId"]
    """<p>The ID of the client application user.</p>"""
    session_id: NotRequired["aws_sdk_lex_runtime_service.types.string.String"]
    """<p>The unique identifier for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSessionResponse) -> dict:
    out: dict = {}
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "bot_alias" in value:
        out["botAlias"] = value["bot_alias"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> DeleteSessionResponse:
    out: DeleteSessionResponse = {}  # type: ignore[typeddict-item]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "botAlias" in data:
        out["bot_alias"] = data["botAlias"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    return out
