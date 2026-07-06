"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamResponseEvent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_lambda._iter import AnyIterator
from aws_sdk_lambda._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_lambda.types.invoke_response_stream_update
    import aws_sdk_lambda.types.invoke_with_response_stream_complete_event


class _InvokeWithResponseStreamResponseEvent_PayloadChunk(TypedDict, closed=True):
    PayloadChunk: (
        "aws_sdk_lambda.types.invoke_response_stream_update.InvokeResponseStreamUpdate"
    )


class _InvokeWithResponseStreamResponseEvent_InvokeComplete(TypedDict, closed=True):
    InvokeComplete: "aws_sdk_lambda.types.invoke_with_response_stream_complete_event.InvokeWithResponseStreamCompleteEvent"


_InvokeWithResponseStreamResponseEvent: TypeAlias = (
    _InvokeWithResponseStreamResponseEvent_PayloadChunk
    | _InvokeWithResponseStreamResponseEvent_InvokeComplete
)
InvokeWithResponseStreamResponseEvent: TypeAlias = AnyIterator[
    _InvokeWithResponseStreamResponseEvent
]


def serialize_event_json(value: _InvokeWithResponseStreamResponseEvent) -> bytes:
    match value:
        case {"PayloadChunk": payload}:
            import aws_sdk_lambda.types.invoke_response_stream_update

            return (
                aws_sdk_lambda.types.invoke_response_stream_update.serialize_event_json(
                    payload
                )
            )
        case {"InvokeComplete": payload}:
            import aws_sdk_lambda.types.invoke_with_response_stream_complete_event

            return aws_sdk_lambda.types.invoke_with_response_stream_complete_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeWithResponseStreamResponseEvent: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _InvokeWithResponseStreamResponseEvent:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "PayloadChunk":
            import aws_sdk_lambda.types.invoke_response_stream_update

            return {
                "PayloadChunk": aws_sdk_lambda.types.invoke_response_stream_update.deserialize_event_json(
                    message
                )
            }
        case "InvokeComplete":
            import aws_sdk_lambda.types.invoke_with_response_stream_complete_event

            return {
                "InvokeComplete": aws_sdk_lambda.types.invoke_with_response_stream_complete_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeWithResponseStreamResponseEvent: unrecognized event-type {event_type!r}"
            )
