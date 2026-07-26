"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#RequestStreamEvent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_runtime_http2._iter import AnyIterator
from capo_sagemaker_runtime_http2._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_sagemaker_runtime_http2.types.request_payload_part


class _RequestStreamEvent_PayloadPart(TypedDict, closed=True):
    PayloadPart: (
        "capo_sagemaker_runtime_http2.types.request_payload_part.RequestPayloadPart"
    )


_RequestStreamEvent: TypeAlias = _RequestStreamEvent_PayloadPart
RequestStreamEvent: TypeAlias = AnyIterator[_RequestStreamEvent]


def serialize_event_json(value: _RequestStreamEvent) -> bytes:
    match value:
        case {"PayloadPart": payload}:
            import capo_sagemaker_runtime_http2.types.request_payload_part

            return capo_sagemaker_runtime_http2.types.request_payload_part.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"RequestStreamEvent: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _RequestStreamEvent:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "PayloadPart":
            import capo_sagemaker_runtime_http2.types.request_payload_part

            return {
                "PayloadPart": capo_sagemaker_runtime_http2.types.request_payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"RequestStreamEvent: unrecognized event-type {event_type!r}"
            )
