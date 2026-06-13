"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_runtime.errors.model_stream_error_exception
    import aws_sdk_bedrock_runtime.errors.model_timeout_exception
    import aws_sdk_bedrock_runtime.errors.service_unavailable_exception
    import aws_sdk_bedrock_runtime.errors.throttling_exception
    import aws_sdk_bedrock_runtime.errors.validation_exception
    import aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part


class _InvokeModelWithBidirectionalStreamOutput_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part.BidirectionalOutputPayloadPart"


class _InvokeModelWithBidirectionalStreamOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_runtime.errors.internal_server_exception.InternalServerException_"


class _InvokeModelWithBidirectionalStreamOutput_modelStreamErrorException(TypedDict):
    modelStreamErrorException: "aws_sdk_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _InvokeModelWithBidirectionalStreamOutput_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_modelTimeoutException(TypedDict):
    modelTimeoutException: (
        "aws_sdk_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_serviceUnavailableException(TypedDict):
    serviceUnavailableException: "aws_sdk_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


InvokeModelWithBidirectionalStreamOutput: TypeAlias = (
    _InvokeModelWithBidirectionalStreamOutput_chunk
    | _InvokeModelWithBidirectionalStreamOutput_internalServerException
    | _InvokeModelWithBidirectionalStreamOutput_modelStreamErrorException
    | _InvokeModelWithBidirectionalStreamOutput_validationException
    | _InvokeModelWithBidirectionalStreamOutput_throttlingException
    | _InvokeModelWithBidirectionalStreamOutput_modelTimeoutException
    | _InvokeModelWithBidirectionalStreamOutput_serviceUnavailableException
)


# --- restJson1 ser/de ---
def serialize_json(value: InvokeModelWithBidirectionalStreamOutput) -> dict:
    if "chunk" in value:
        import aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part

        return {
            "chunk": aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part.serialize_json(
                value["chunk"]
            )
        }
    elif "internalServerException" in value:
        import aws_sdk_bedrock_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_runtime.errors.internal_server_exception.serialize_json(
                value["internalServerException"]
            )
        }
    elif "modelStreamErrorException" in value:
        import aws_sdk_bedrock_runtime.errors.model_stream_error_exception

        return {
            "modelStreamErrorException": aws_sdk_bedrock_runtime.errors.model_stream_error_exception.serialize_json(
                value["modelStreamErrorException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_bedrock_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_runtime.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    elif "throttlingException" in value:
        import aws_sdk_bedrock_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_runtime.errors.throttling_exception.serialize_json(
                value["throttlingException"]
            )
        }
    elif "modelTimeoutException" in value:
        import aws_sdk_bedrock_runtime.errors.model_timeout_exception

        return {
            "modelTimeoutException": aws_sdk_bedrock_runtime.errors.model_timeout_exception.serialize_json(
                value["modelTimeoutException"]
            )
        }
    elif "serviceUnavailableException" in value:
        import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

        return {
            "serviceUnavailableException": aws_sdk_bedrock_runtime.errors.service_unavailable_exception.serialize_json(
                value["serviceUnavailableException"]
            )
        }
    else:
        raise SerializationError(
            "InvokeModelWithBidirectionalStreamOutput: no variant present"
        )


def deserialize_json(data: dict) -> InvokeModelWithBidirectionalStreamOutput:
    if "chunk" in data:
        import aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part

        return {
            "chunk": aws_sdk_bedrock_runtime.types.bidirectional_output_payload_part.deserialize_json(
                data["chunk"]
            )
        }
    elif "internalServerException" in data:
        import aws_sdk_bedrock_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_runtime.errors.internal_server_exception.deserialize_json(
                data["internalServerException"]
            )
        }
    elif "modelStreamErrorException" in data:
        import aws_sdk_bedrock_runtime.errors.model_stream_error_exception

        return {
            "modelStreamErrorException": aws_sdk_bedrock_runtime.errors.model_stream_error_exception.deserialize_json(
                data["modelStreamErrorException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_bedrock_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_runtime.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    elif "throttlingException" in data:
        import aws_sdk_bedrock_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_runtime.errors.throttling_exception.deserialize_json(
                data["throttlingException"]
            )
        }
    elif "modelTimeoutException" in data:
        import aws_sdk_bedrock_runtime.errors.model_timeout_exception

        return {
            "modelTimeoutException": aws_sdk_bedrock_runtime.errors.model_timeout_exception.deserialize_json(
                data["modelTimeoutException"]
            )
        }
    elif "serviceUnavailableException" in data:
        import aws_sdk_bedrock_runtime.errors.service_unavailable_exception

        return {
            "serviceUnavailableException": aws_sdk_bedrock_runtime.errors.service_unavailable_exception.deserialize_json(
                data["serviceUnavailableException"]
            )
        }
    else:
        raise DeserializationError(
            "InvokeModelWithBidirectionalStreamOutput: no recognized variant key"
        )
