"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ResponseStreamEvent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker_runtime_http2.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure
    import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error
    import aws_sdk_sagemaker_runtime_http2.types.response_payload_part


class _ResponseStreamEvent_PayloadPart(TypedDict):
    PayloadPart: "aws_sdk_sagemaker_runtime_http2.types.response_payload_part.ResponsePayloadPart"


class _ResponseStreamEvent_ModelStreamError(TypedDict):
    ModelStreamError: (
        "aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError"
    )


class _ResponseStreamEvent_InternalStreamFailure(TypedDict):
    InternalStreamFailure: "aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure"


ResponseStreamEvent: TypeAlias = (
    _ResponseStreamEvent_PayloadPart
    | _ResponseStreamEvent_ModelStreamError
    | _ResponseStreamEvent_InternalStreamFailure
)


# --- restJson1 ser/de ---
def serialize_json(value: ResponseStreamEvent) -> dict:
    if "PayloadPart" in value:
        import aws_sdk_sagemaker_runtime_http2.types.response_payload_part

        return {
            "PayloadPart": aws_sdk_sagemaker_runtime_http2.types.response_payload_part.serialize_json(
                value["PayloadPart"]
            )
        }
    elif "ModelStreamError" in value:
        import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error

        return {
            "ModelStreamError": aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.serialize_json(
                value["ModelStreamError"]
            )
        }
    elif "InternalStreamFailure" in value:
        import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure

        return {
            "InternalStreamFailure": aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.serialize_json(
                value["InternalStreamFailure"]
            )
        }
    else:
        raise SerializationError("ResponseStreamEvent: no variant present")


def deserialize_json(data: dict) -> ResponseStreamEvent:
    if "PayloadPart" in data:
        import aws_sdk_sagemaker_runtime_http2.types.response_payload_part

        return {
            "PayloadPart": aws_sdk_sagemaker_runtime_http2.types.response_payload_part.deserialize_json(
                data["PayloadPart"]
            )
        }
    elif "ModelStreamError" in data:
        import aws_sdk_sagemaker_runtime_http2.errors.model_stream_error

        return {
            "ModelStreamError": aws_sdk_sagemaker_runtime_http2.errors.model_stream_error.deserialize_json(
                data["ModelStreamError"]
            )
        }
    elif "InternalStreamFailure" in data:
        import aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure

        return {
            "InternalStreamFailure": aws_sdk_sagemaker_runtime_http2.errors.internal_stream_failure.deserialize_json(
                data["InternalStreamFailure"]
            )
        }
    else:
        raise DeserializationError("ResponseStreamEvent: no recognized variant key")
