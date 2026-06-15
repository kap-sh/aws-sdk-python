"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommandStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.errors.access_denied_exception
    import aws_sdk_bedrock_agentcore.errors.internal_server_exception
    import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
    import aws_sdk_bedrock_agentcore.errors.runtime_client_error
    import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agentcore.errors.throttling_exception
    import aws_sdk_bedrock_agentcore.errors.validation_exception
    import aws_sdk_bedrock_agentcore.types.response_chunk


class _InvokeAgentRuntimeCommandStreamOutput_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_agentcore.types.response_chunk.ResponseChunk"


class _InvokeAgentRuntimeCommandStreamOutput_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException_"


class _InvokeAgentRuntimeCommandStreamOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _InvokeAgentRuntimeCommandStreamOutput_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException_"


class _InvokeAgentRuntimeCommandStreamOutput_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _InvokeAgentRuntimeCommandStreamOutput_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_runtimeClientError(TypedDict):
    runtimeClientError: (
        "aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError_"
    )


InvokeAgentRuntimeCommandStreamOutput: TypeAlias = (
    _InvokeAgentRuntimeCommandStreamOutput_chunk
    | _InvokeAgentRuntimeCommandStreamOutput_accessDeniedException
    | _InvokeAgentRuntimeCommandStreamOutput_internalServerException
    | _InvokeAgentRuntimeCommandStreamOutput_resourceNotFoundException
    | _InvokeAgentRuntimeCommandStreamOutput_serviceQuotaExceededException
    | _InvokeAgentRuntimeCommandStreamOutput_throttlingException
    | _InvokeAgentRuntimeCommandStreamOutput_validationException
    | _InvokeAgentRuntimeCommandStreamOutput_runtimeClientError
)


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAgentRuntimeCommandStreamOutput) -> dict:
    if "chunk" in value:
        import aws_sdk_bedrock_agentcore.types.response_chunk

        return {
            "chunk": aws_sdk_bedrock_agentcore.types.response_chunk.serialize_json(
                value["chunk"]
            )
        }
    elif "accessDeniedException" in value:
        import aws_sdk_bedrock_agentcore.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_bedrock_agentcore.errors.access_denied_exception.serialize_json(
                value["accessDeniedException"]
            )
        }
    elif "internalServerException" in value:
        import aws_sdk_bedrock_agentcore.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agentcore.errors.internal_server_exception.serialize_json(
                value["internalServerException"]
            )
        }
    elif "resourceNotFoundException" in value:
        import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception

        return {
            "resourceNotFoundException": aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.serialize_json(
                value["resourceNotFoundException"]
            )
        }
    elif "serviceQuotaExceededException" in value:
        import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception

        return {
            "serviceQuotaExceededException": aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.serialize_json(
                value["serviceQuotaExceededException"]
            )
        }
    elif "throttlingException" in value:
        import aws_sdk_bedrock_agentcore.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_agentcore.errors.throttling_exception.serialize_json(
                value["throttlingException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_bedrock_agentcore.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agentcore.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    elif "runtimeClientError" in value:
        import aws_sdk_bedrock_agentcore.errors.runtime_client_error

        return {
            "runtimeClientError": aws_sdk_bedrock_agentcore.errors.runtime_client_error.serialize_json(
                value["runtimeClientError"]
            )
        }
    else:
        raise SerializationError(
            "InvokeAgentRuntimeCommandStreamOutput: no variant present"
        )


def deserialize_json(data: dict) -> InvokeAgentRuntimeCommandStreamOutput:
    if "chunk" in data:
        import aws_sdk_bedrock_agentcore.types.response_chunk

        return {
            "chunk": aws_sdk_bedrock_agentcore.types.response_chunk.deserialize_json(
                data["chunk"]
            )
        }
    elif "accessDeniedException" in data:
        import aws_sdk_bedrock_agentcore.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_bedrock_agentcore.errors.access_denied_exception.deserialize_json(
                data["accessDeniedException"]
            )
        }
    elif "internalServerException" in data:
        import aws_sdk_bedrock_agentcore.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agentcore.errors.internal_server_exception.deserialize_json(
                data["internalServerException"]
            )
        }
    elif "resourceNotFoundException" in data:
        import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception

        return {
            "resourceNotFoundException": aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.deserialize_json(
                data["resourceNotFoundException"]
            )
        }
    elif "serviceQuotaExceededException" in data:
        import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception

        return {
            "serviceQuotaExceededException": aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.deserialize_json(
                data["serviceQuotaExceededException"]
            )
        }
    elif "throttlingException" in data:
        import aws_sdk_bedrock_agentcore.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_agentcore.errors.throttling_exception.deserialize_json(
                data["throttlingException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_bedrock_agentcore.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agentcore.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    elif "runtimeClientError" in data:
        import aws_sdk_bedrock_agentcore.errors.runtime_client_error

        return {
            "runtimeClientError": aws_sdk_bedrock_agentcore.errors.runtime_client_error.deserialize_json(
                data["runtimeClientError"]
            )
        }
    else:
        raise DeserializationError(
            "InvokeAgentRuntimeCommandStreamOutput: no recognized variant key"
        )
