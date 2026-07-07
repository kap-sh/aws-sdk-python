"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ResponseStreamEvent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker_runtime_http2._iter import AnyIterator
from aws_sdk_sagemaker_runtime_http2._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure
    import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error
    import aws_sdk_sagemaker_runtime_http2.types.response_payload_part


class _ResponseStreamEvent_PayloadPart(TypedDict, closed=True):
    PayloadPart: "aws_sdk_sagemaker_runtime_http2.types.response_payload_part.ResponsePayloadPart"


class _ResponseStreamEvent_ModelStreamError(TypedDict, closed=True):
    ModelStreamError: (
        "aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError_"
    )


class _ResponseStreamEvent_InternalStreamFailure(TypedDict, closed=True):
    InternalStreamFailure: "aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure_"


_ResponseStreamEvent: TypeAlias = (
    _ResponseStreamEvent_PayloadPart
    | _ResponseStreamEvent_ModelStreamError
    | _ResponseStreamEvent_InternalStreamFailure
)
ResponseStreamEvent: TypeAlias = AnyIterator[_ResponseStreamEvent]


def serialize_event_json(value: _ResponseStreamEvent) -> bytes:
    match value:
        case {"PayloadPart": payload}:
            import aws_sdk_sagemaker_runtime_http2.types.response_payload_part

            return aws_sdk_sagemaker_runtime_http2.types.response_payload_part.serialize_event_json(
                payload
            )
        case {"ModelStreamError": payload}:
            import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error

            return aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.serialize_event_json(
                payload
            )
        case {"InternalStreamFailure": payload}:
            import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure

            return aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ResponseStreamEvent: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ResponseStreamEvent:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "ModelStreamError":
                import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error

                raise aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError(
                    aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.deserialize_event_json(
                        message
                    )
                )
            case "InternalStreamFailure":
                import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure

                raise aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure(
                    aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"ResponseStreamEvent: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "PayloadPart":
            import aws_sdk_sagemaker_runtime_http2.types.response_payload_part

            return {
                "PayloadPart": aws_sdk_sagemaker_runtime_http2.types.response_payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"ResponseStreamEvent: unrecognized event-type {event_type!r}"
            )
