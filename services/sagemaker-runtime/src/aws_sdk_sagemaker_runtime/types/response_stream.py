"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker_runtime.errors import DeserializationError, SerializationError

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


ResponseStream: TypeAlias = (
    _ResponseStream_PayloadPart
    | _ResponseStream_ModelStreamError
    | _ResponseStream_InternalStreamFailure
)


# --- restJson1 ser/de ---
def serialize_json(value: ResponseStream) -> dict:
    if "PayloadPart" in value:
        import aws_sdk_sagemaker_runtime.types.payload_part

        return {
            "PayloadPart": aws_sdk_sagemaker_runtime.types.payload_part.serialize_json(
                value["PayloadPart"]
            )
        }
    elif "ModelStreamError" in value:
        import aws_sdk_sagemaker_runtime.errors.model_stream_error

        return {
            "ModelStreamError": aws_sdk_sagemaker_runtime.errors.model_stream_error.serialize_json(
                value["ModelStreamError"]
            )
        }
    elif "InternalStreamFailure" in value:
        import aws_sdk_sagemaker_runtime.errors.internal_stream_failure

        return {
            "InternalStreamFailure": aws_sdk_sagemaker_runtime.errors.internal_stream_failure.serialize_json(
                value["InternalStreamFailure"]
            )
        }
    else:
        raise SerializationError("ResponseStream: no variant present")


def deserialize_json(data: dict) -> ResponseStream:
    if "PayloadPart" in data:
        import aws_sdk_sagemaker_runtime.types.payload_part

        return {
            "PayloadPart": aws_sdk_sagemaker_runtime.types.payload_part.deserialize_json(
                data["PayloadPart"]
            )
        }
    elif "ModelStreamError" in data:
        import aws_sdk_sagemaker_runtime.errors.model_stream_error

        return {
            "ModelStreamError": aws_sdk_sagemaker_runtime.errors.model_stream_error.deserialize_json(
                data["ModelStreamError"]
            )
        }
    elif "InternalStreamFailure" in data:
        import aws_sdk_sagemaker_runtime.errors.internal_stream_failure

        return {
            "InternalStreamFailure": aws_sdk_sagemaker_runtime.errors.internal_stream_failure.deserialize_json(
                data["InternalStreamFailure"]
            )
        }
    else:
        raise DeserializationError("ResponseStream: no recognized variant key")
