"""Generated from Smithy shape ``com.amazonaws.qconnect#GetNextMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.conversation_state
    import aws_sdk_qconnect.types.message_output
    import aws_sdk_qconnect.types.message_type
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.runtime_session_data_list
    import aws_sdk_qconnect.types.uuid


class GetNextMessageResponse(TypedDict, closed=True):
    type: "aws_sdk_qconnect.types.message_type.MessageType"
    """<p>The type of message response.</p>"""
    response: "aws_sdk_qconnect.types.message_output.MessageOutput"
    """<p>The message response to the requested message.</p>"""
    request_message_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the submitted message.</p>"""
    conversation_state: "aws_sdk_qconnect.types.conversation_state.ConversationState"
    """<p>The state of current conversation.</p>"""
    next_message_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next message.</p>"""
    conversation_session_data: NotRequired[
        "aws_sdk_qconnect.types.runtime_session_data_list.RuntimeSessionDataList"
    ]
    """<p>The conversation data stored on an Amazon Q in Connect Session.</p>"""
    chunked_response_terminated: NotRequired["bool"]
    """<p>Indicates whether the chunked response has been terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNextMessageResponse) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import aws_sdk_qconnect.types.message_output

    out["response"] = aws_sdk_qconnect.types.message_output.serialize_json(
        value["response"]
    )
    out["requestMessageId"] = value["request_message_id"]
    import aws_sdk_qconnect.types.conversation_state

    out["conversationState"] = aws_sdk_qconnect.types.conversation_state.serialize_json(
        value["conversation_state"]
    )
    if "next_message_token" in value:
        out["nextMessageToken"] = value["next_message_token"]
    if "conversation_session_data" in value:
        import aws_sdk_qconnect.types.runtime_session_data_list

        out["conversationSessionData"] = (
            aws_sdk_qconnect.types.runtime_session_data_list.serialize_json(
                value["conversation_session_data"]
            )
        )
    if "chunked_response_terminated" in value:
        out["chunkedResponseTerminated"] = value["chunked_response_terminated"]
    return out


def deserialize_json(data: dict) -> GetNextMessageResponse:
    out: GetNextMessageResponse = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GetNextMessageResponse.type required")
    if "response" in data:
        import aws_sdk_qconnect.types.message_output

        out["response"] = aws_sdk_qconnect.types.message_output.deserialize_json(
            data["response"]
        )
    else:
        raise DeserializationError("GetNextMessageResponse.response required")
    if "requestMessageId" in data:
        out["request_message_id"] = data["requestMessageId"]
    else:
        raise DeserializationError("GetNextMessageResponse.request_message_id required")
    if "conversationState" in data:
        import aws_sdk_qconnect.types.conversation_state

        out["conversation_state"] = (
            aws_sdk_qconnect.types.conversation_state.deserialize_json(
                data["conversationState"]
            )
        )
    else:
        raise DeserializationError("GetNextMessageResponse.conversation_state required")
    if "nextMessageToken" in data:
        out["next_message_token"] = data["nextMessageToken"]
    if "conversationSessionData" in data:
        import aws_sdk_qconnect.types.runtime_session_data_list

        out["conversation_session_data"] = (
            aws_sdk_qconnect.types.runtime_session_data_list.deserialize_json(
                data["conversationSessionData"]
            )
        )
    if "chunkedResponseTerminated" in data:
        out["chunked_response_terminated"] = data["chunkedResponseTerminated"]
    return out
