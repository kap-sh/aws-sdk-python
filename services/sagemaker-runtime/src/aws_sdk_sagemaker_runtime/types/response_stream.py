"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker_runtime._iter import AnyIterator
from aws_sdk_sagemaker_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.errors.internal_stream_failure
    import aws_sdk_sagemaker_runtime.errors.model_stream_error
    import aws_sdk_sagemaker_runtime.types.payload_part


class _ResponseStream_PayloadPart(TypedDict):
    PayloadPart: "aws_sdk_sagemaker_runtime.types.payload_part.PayloadPart"


class _ResponseStream_ModelStreamError(TypedDict):
    ModelStreamError: (
        "aws_sdk_sagemaker_runtime.errors.model_stream_error.ModelStreamError_"
    )


class _ResponseStream_InternalStreamFailure(TypedDict):
    InternalStreamFailure: "aws_sdk_sagemaker_runtime.errors.internal_stream_failure.InternalStreamFailure_"


_ResponseStream: TypeAlias = (
    _ResponseStream_PayloadPart
    | _ResponseStream_ModelStreamError
    | _ResponseStream_InternalStreamFailure
)
ResponseStream: TypeAlias = AnyIterator[_ResponseStream]


def serialize_event_json(value: _ResponseStream) -> bytes:
    match value:
        case {"PayloadPart": payload}:
            import aws_sdk_sagemaker_runtime.types.payload_part

            return aws_sdk_sagemaker_runtime.types.payload_part.serialize_event_json(
                payload
            )
        case {"ModelStreamError": payload}:
            import aws_sdk_sagemaker_runtime.errors.model_stream_error

            return aws_sdk_sagemaker_runtime.errors.model_stream_error.serialize_event_json(
                payload
            )
        case {"InternalStreamFailure": payload}:
            import aws_sdk_sagemaker_runtime.errors.internal_stream_failure

            return aws_sdk_sagemaker_runtime.errors.internal_stream_failure.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "ModelStreamError":
                import aws_sdk_sagemaker_runtime.errors.model_stream_error

                raise aws_sdk_sagemaker_runtime.errors.model_stream_error.ModelStreamError(
                    aws_sdk_sagemaker_runtime.errors.model_stream_error.deserialize_event_json(
                        message
                    )
                )
            case "InternalStreamFailure":
                import aws_sdk_sagemaker_runtime.errors.internal_stream_failure

                raise aws_sdk_sagemaker_runtime.errors.internal_stream_failure.InternalStreamFailure(
                    aws_sdk_sagemaker_runtime.errors.internal_stream_failure.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"ResponseStream: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "PayloadPart":
            import aws_sdk_sagemaker_runtime.types.payload_part

            return {
                "PayloadPart": aws_sdk_sagemaker_runtime.types.payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
