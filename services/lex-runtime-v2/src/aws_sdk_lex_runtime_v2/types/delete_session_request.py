"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DeleteSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.bot_alias_identifier
    import aws_sdk_lex_runtime_v2.types.bot_identifier
    import aws_sdk_lex_runtime_v2.types.locale_id
    import aws_sdk_lex_runtime_v2.types.session_id


class DeleteSessionRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_runtime_v2.types.bot_identifier.BotIdentifier"
    """<p>The identifier of the bot that contains the session data.</p>"""
    bot_alias_id: "aws_sdk_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier"
    """<p>The alias identifier in use for the bot that contains the session data.</p>"""
    locale_id: "aws_sdk_lex_runtime_v2.types.locale_id.LocaleId"
    """<p>The locale where the session is in use.</p>"""
    session_id: "aws_sdk_lex_runtime_v2.types.session_id.SessionId"
    """<p>The identifier of the session to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSessionRequest:
    out: DeleteSessionRequest = {}  # type: ignore[typeddict-item]
    return out
