"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeTextRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.bot_alias_identifier
    import aws_sdk_lex_runtime_v2.types.bot_identifier
    import aws_sdk_lex_runtime_v2.types.locale_id
    import aws_sdk_lex_runtime_v2.types.session_id
    import aws_sdk_lex_runtime_v2.types.session_state
    import aws_sdk_lex_runtime_v2.types.string_map
    import aws_sdk_lex_runtime_v2.types.text


class RecognizeTextRequest(TypedDict):
    bot_id: "aws_sdk_lex_runtime_v2.types.bot_identifier.BotIdentifier"
    """<p>The identifier of the bot that processes the request.</p>"""
    bot_alias_id: "aws_sdk_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier"
    """<p>The alias identifier in use for the bot that processes the request.</p>"""
    locale_id: "aws_sdk_lex_runtime_v2.types.locale_id.LocaleId"
    """<p>The locale where the session is in use.</p>"""
    session_id: "aws_sdk_lex_runtime_v2.types.session_id.SessionId"
    """<p>The identifier of the user session that is having the conversation.</p>"""
    text: "aws_sdk_lex_runtime_v2.types.text.Text"
    """<p>The text that the user entered. Amazon Lex V2 interprets this text.</p>"""
    session_state: NotRequired[
        "aws_sdk_lex_runtime_v2.types.session_state.SessionState"
    ]
    """<p>The current state of the dialog between the user and the bot.</p>"""
    request_attributes: NotRequired["aws_sdk_lex_runtime_v2.types.string_map.StringMap"]
    """<p>Request-specific information passed between the client application and Amazon Lex V2 </p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecognizeTextRequest) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "session_state" in value:
        import aws_sdk_lex_runtime_v2.types.session_state

        out["sessionState"] = aws_sdk_lex_runtime_v2.types.session_state.serialize_json(
            value["session_state"]
        )
    if "request_attributes" in value:
        import aws_sdk_lex_runtime_v2.types.string_map

        out["requestAttributes"] = (
            aws_sdk_lex_runtime_v2.types.string_map.serialize_json(
                value["request_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecognizeTextRequest:
    out: RecognizeTextRequest = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("RecognizeTextRequest.text required")
    if "sessionState" in data:
        import aws_sdk_lex_runtime_v2.types.session_state

        out["session_state"] = (
            aws_sdk_lex_runtime_v2.types.session_state.deserialize_json(
                data["sessionState"]
            )
        )
    if "requestAttributes" in data:
        import aws_sdk_lex_runtime_v2.types.string_map

        out["request_attributes"] = (
            aws_sdk_lex_runtime_v2.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    return out
