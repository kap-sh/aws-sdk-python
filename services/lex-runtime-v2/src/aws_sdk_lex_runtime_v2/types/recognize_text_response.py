"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeTextResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.interpretations
    import aws_sdk_lex_runtime_v2.types.messages
    import aws_sdk_lex_runtime_v2.types.recognized_bot_member
    import aws_sdk_lex_runtime_v2.types.session_id
    import aws_sdk_lex_runtime_v2.types.session_state
    import aws_sdk_lex_runtime_v2.types.string_map


class RecognizeTextResponse(TypedDict):
    messages: NotRequired["aws_sdk_lex_runtime_v2.types.messages.Messages"]
    """<p>A list of messages last sent to the user. The messages are ordered based on the order that you returned the messages from your Lambda function or the order that the messages are defined in the bot.</p>"""
    session_state: NotRequired[
        "aws_sdk_lex_runtime_v2.types.session_state.SessionState"
    ]
    """<p>Represents the current state of the dialog between the user and the bot. </p> <p>Use this to determine the progress of the conversation and what the next action may be.</p>"""
    interpretations: NotRequired[
        "aws_sdk_lex_runtime_v2.types.interpretations.Interpretations"
    ]
    """<p>A list of intents that Amazon Lex V2 determined might satisfy the user's utterance. </p> <p>Each interpretation includes the intent, a score that indicates now confident Amazon Lex V2 is that the interpretation is the correct one, and an optional sentiment response that indicates the sentiment expressed in the utterance.</p>"""
    request_attributes: NotRequired["aws_sdk_lex_runtime_v2.types.string_map.StringMap"]
    """<p>The attributes sent in the request.</p>"""
    session_id: NotRequired["aws_sdk_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the session in use.</p>"""
    recognized_bot_member: NotRequired[
        "aws_sdk_lex_runtime_v2.types.recognized_bot_member.RecognizedBotMember"
    ]
    """<p>The bot member that recognized the text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecognizeTextResponse) -> dict:
    out: dict = {}
    if "messages" in value:
        import aws_sdk_lex_runtime_v2.types.messages

        out["messages"] = aws_sdk_lex_runtime_v2.types.messages.serialize_json(
            value["messages"]
        )
    if "session_state" in value:
        import aws_sdk_lex_runtime_v2.types.session_state

        out["sessionState"] = aws_sdk_lex_runtime_v2.types.session_state.serialize_json(
            value["session_state"]
        )
    if "interpretations" in value:
        import aws_sdk_lex_runtime_v2.types.interpretations

        out["interpretations"] = (
            aws_sdk_lex_runtime_v2.types.interpretations.serialize_json(
                value["interpretations"]
            )
        )
    if "request_attributes" in value:
        import aws_sdk_lex_runtime_v2.types.string_map

        out["requestAttributes"] = (
            aws_sdk_lex_runtime_v2.types.string_map.serialize_json(
                value["request_attributes"]
            )
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "recognized_bot_member" in value:
        import aws_sdk_lex_runtime_v2.types.recognized_bot_member

        out["recognizedBotMember"] = (
            aws_sdk_lex_runtime_v2.types.recognized_bot_member.serialize_json(
                value["recognized_bot_member"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecognizeTextResponse:
    out: RecognizeTextResponse = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_lex_runtime_v2.types.messages

        out["messages"] = aws_sdk_lex_runtime_v2.types.messages.deserialize_json(
            data["messages"]
        )
    if "sessionState" in data:
        import aws_sdk_lex_runtime_v2.types.session_state

        out["session_state"] = (
            aws_sdk_lex_runtime_v2.types.session_state.deserialize_json(
                data["sessionState"]
            )
        )
    if "interpretations" in data:
        import aws_sdk_lex_runtime_v2.types.interpretations

        out["interpretations"] = (
            aws_sdk_lex_runtime_v2.types.interpretations.deserialize_json(
                data["interpretations"]
            )
        )
    if "requestAttributes" in data:
        import aws_sdk_lex_runtime_v2.types.string_map

        out["request_attributes"] = (
            aws_sdk_lex_runtime_v2.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "recognizedBotMember" in data:
        import aws_sdk_lex_runtime_v2.types.recognized_bot_member

        out["recognized_bot_member"] = (
            aws_sdk_lex_runtime_v2.types.recognized_bot_member.deserialize_json(
                data["recognizedBotMember"]
            )
        )
    return out
