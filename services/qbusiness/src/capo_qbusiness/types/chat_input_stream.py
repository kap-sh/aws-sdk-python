"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatInputStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness._iter import AnyIterator
from capo_qbusiness._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution_event
    import capo_qbusiness.types.attachment_input_event
    import capo_qbusiness.types.auth_challenge_response_event
    import capo_qbusiness.types.configuration_event
    import capo_qbusiness.types.end_of_input_event
    import capo_qbusiness.types.text_input_event


class _ChatInputStream_configurationEvent(TypedDict, closed=True):
    configurationEvent: "capo_qbusiness.types.configuration_event.ConfigurationEvent"


class _ChatInputStream_textEvent(TypedDict, closed=True):
    textEvent: "capo_qbusiness.types.text_input_event.TextInputEvent"


class _ChatInputStream_attachmentEvent(TypedDict, closed=True):
    attachmentEvent: "capo_qbusiness.types.attachment_input_event.AttachmentInputEvent"


class _ChatInputStream_actionExecutionEvent(TypedDict, closed=True):
    actionExecutionEvent: (
        "capo_qbusiness.types.action_execution_event.ActionExecutionEvent"
    )


class _ChatInputStream_endOfInputEvent(TypedDict, closed=True):
    endOfInputEvent: "capo_qbusiness.types.end_of_input_event.EndOfInputEvent"


class _ChatInputStream_authChallengeResponseEvent(TypedDict, closed=True):
    authChallengeResponseEvent: (
        "capo_qbusiness.types.auth_challenge_response_event.AuthChallengeResponseEvent"
    )


_ChatInputStream: TypeAlias = (
    _ChatInputStream_configurationEvent
    | _ChatInputStream_textEvent
    | _ChatInputStream_attachmentEvent
    | _ChatInputStream_actionExecutionEvent
    | _ChatInputStream_endOfInputEvent
    | _ChatInputStream_authChallengeResponseEvent
)
ChatInputStream: TypeAlias = AnyIterator[_ChatInputStream]


def serialize_event_json(value: _ChatInputStream) -> bytes:
    match value:
        case {"configurationEvent": payload}:
            import capo_qbusiness.types.configuration_event

            return capo_qbusiness.types.configuration_event.serialize_event_json(
                payload
            )
        case {"textEvent": payload}:
            import capo_qbusiness.types.text_input_event

            return capo_qbusiness.types.text_input_event.serialize_event_json(payload)
        case {"attachmentEvent": payload}:
            import capo_qbusiness.types.attachment_input_event

            return capo_qbusiness.types.attachment_input_event.serialize_event_json(
                payload
            )
        case {"actionExecutionEvent": payload}:
            import capo_qbusiness.types.action_execution_event

            return capo_qbusiness.types.action_execution_event.serialize_event_json(
                payload
            )
        case {"endOfInputEvent": payload}:
            import capo_qbusiness.types.end_of_input_event

            return capo_qbusiness.types.end_of_input_event.serialize_event_json(payload)
        case {"authChallengeResponseEvent": payload}:
            import capo_qbusiness.types.auth_challenge_response_event

            return (
                capo_qbusiness.types.auth_challenge_response_event.serialize_event_json(
                    payload
                )
            )
        case _:
            raise ValueError(f"ChatInputStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ChatInputStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "configurationEvent":
            import capo_qbusiness.types.configuration_event

            return {
                "configurationEvent": capo_qbusiness.types.configuration_event.deserialize_event_json(
                    message
                )
            }
        case "textEvent":
            import capo_qbusiness.types.text_input_event

            return {
                "textEvent": capo_qbusiness.types.text_input_event.deserialize_event_json(
                    message
                )
            }
        case "attachmentEvent":
            import capo_qbusiness.types.attachment_input_event

            return {
                "attachmentEvent": capo_qbusiness.types.attachment_input_event.deserialize_event_json(
                    message
                )
            }
        case "actionExecutionEvent":
            import capo_qbusiness.types.action_execution_event

            return {
                "actionExecutionEvent": capo_qbusiness.types.action_execution_event.deserialize_event_json(
                    message
                )
            }
        case "endOfInputEvent":
            import capo_qbusiness.types.end_of_input_event

            return {
                "endOfInputEvent": capo_qbusiness.types.end_of_input_event.deserialize_event_json(
                    message
                )
            }
        case "authChallengeResponseEvent":
            import capo_qbusiness.types.auth_challenge_response_event

            return {
                "authChallengeResponseEvent": capo_qbusiness.types.auth_challenge_response_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ChatInputStream: unrecognized event-type {event_type!r}")
