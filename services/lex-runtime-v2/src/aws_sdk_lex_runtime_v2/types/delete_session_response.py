"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DeleteSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.bot_alias_identifier
    import aws_sdk_lex_runtime_v2.types.bot_identifier
    import aws_sdk_lex_runtime_v2.types.locale_id
    import aws_sdk_lex_runtime_v2.types.session_id


class DeleteSessionResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_runtime_v2.types.bot_identifier.BotIdentifier"]
    """<p>The identifier of the bot that contained the session data.</p>"""
    bot_alias_id: NotRequired[
        "aws_sdk_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier"
    ]
    """<p>The alias identifier in use for the bot that contained the session data.</p>"""
    locale_id: NotRequired["aws_sdk_lex_runtime_v2.types.locale_id.LocaleId"]
    """<p>The locale where the session was used.</p>"""
    session_id: NotRequired["aws_sdk_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the deleted session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSessionResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> DeleteSessionResponse:
    out: DeleteSessionResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    return out
