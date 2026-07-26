"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DeleteSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.bot_alias
    import capo_lex_runtime_service.types.bot_name
    import capo_lex_runtime_service.types.user_id


class DeleteSessionRequest(TypedDict, closed=True):
    bot_name: "capo_lex_runtime_service.types.bot_name.BotName"
    """<p>The name of the bot that contains the session data.</p>"""
    bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias"
    """<p>The alias in use for the bot that contains the session data.</p>"""
    user_id: "capo_lex_runtime_service.types.user_id.UserId"
    """<p>The identifier of the user associated with the session data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSessionRequest:
    out: DeleteSessionRequest = {}  # type: ignore[typeddict-item]
    return out
