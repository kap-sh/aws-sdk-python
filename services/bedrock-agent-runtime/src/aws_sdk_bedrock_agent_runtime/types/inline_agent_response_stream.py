"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
    import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
    import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
    import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
    import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
    import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
    import aws_sdk_bedrock_agent_runtime.errors.validation_exception
    import aws_sdk_bedrock_agent_runtime.types.inline_agent_file_part
    import aws_sdk_bedrock_agent_runtime.types.inline_agent_payload_part
    import aws_sdk_bedrock_agent_runtime.types.inline_agent_return_control_payload
    import aws_sdk_bedrock_agent_runtime.types.inline_agent_trace_part


class _InlineAgentResponseStream_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_agent_runtime.types.inline_agent_payload_part.InlineAgentPayloadPart"


class _InlineAgentResponseStream_trace(TypedDict):
    trace: "aws_sdk_bedrock_agent_runtime.types.inline_agent_trace_part.InlineAgentTracePart"


class _InlineAgentResponseStream_returnControl(TypedDict):
    returnControl: "aws_sdk_bedrock_agent_runtime.types.inline_agent_return_control_payload.InlineAgentReturnControlPayload"


class _InlineAgentResponseStream_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _InlineAgentResponseStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _InlineAgentResponseStream_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _InlineAgentResponseStream_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _InlineAgentResponseStream_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _InlineAgentResponseStream_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _InlineAgentResponseStream_conflictException(TypedDict):
    conflictException: (
        "aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _InlineAgentResponseStream_dependencyFailedException(TypedDict):
    dependencyFailedException: "aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _InlineAgentResponseStream_badGatewayException(TypedDict):
    badGatewayException: "aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"


class _InlineAgentResponseStream_files(TypedDict):
    files: (
        "aws_sdk_bedrock_agent_runtime.types.inline_agent_file_part.InlineAgentFilePart"
    )


InlineAgentResponseStream: TypeAlias = (
    _InlineAgentResponseStream_chunk
    | _InlineAgentResponseStream_trace
    | _InlineAgentResponseStream_returnControl
    | _InlineAgentResponseStream_internalServerException
    | _InlineAgentResponseStream_validationException
    | _InlineAgentResponseStream_resourceNotFoundException
    | _InlineAgentResponseStream_serviceQuotaExceededException
    | _InlineAgentResponseStream_throttlingException
    | _InlineAgentResponseStream_accessDeniedException
    | _InlineAgentResponseStream_conflictException
    | _InlineAgentResponseStream_dependencyFailedException
    | _InlineAgentResponseStream_badGatewayException
    | _InlineAgentResponseStream_files
)


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentResponseStream) -> dict:
    if "chunk" in value:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_payload_part

        return {
            "chunk": aws_sdk_bedrock_agent_runtime.types.inline_agent_payload_part.serialize_json(
                value["chunk"]
            )
        }
    elif "trace" in value:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_trace_part

        return {
            "trace": aws_sdk_bedrock_agent_runtime.types.inline_agent_trace_part.serialize_json(
                value["trace"]
            )
        }
    elif "returnControl" in value:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_return_control_payload

        return {
            "returnControl": aws_sdk_bedrock_agent_runtime.types.inline_agent_return_control_payload.serialize_json(
                value["returnControl"]
            )
        }
    elif "internalServerException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.serialize_json(
                value["internalServerException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agent_runtime.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    elif "resourceNotFoundException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception

        return {
            "resourceNotFoundException": aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.serialize_json(
                value["resourceNotFoundException"]
            )
        }
    elif "serviceQuotaExceededException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception

        return {
            "serviceQuotaExceededException": aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.serialize_json(
                value["serviceQuotaExceededException"]
            )
        }
    elif "throttlingException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_agent_runtime.errors.throttling_exception.serialize_json(
                value["throttlingException"]
            )
        }
    elif "accessDeniedException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.serialize_json(
                value["accessDeniedException"]
            )
        }
    elif "conflictException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.conflict_exception

        return {
            "conflictException": aws_sdk_bedrock_agent_runtime.errors.conflict_exception.serialize_json(
                value["conflictException"]
            )
        }
    elif "dependencyFailedException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception

        return {
            "dependencyFailedException": aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_json(
                value["dependencyFailedException"]
            )
        }
    elif "badGatewayException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception

        return {
            "badGatewayException": aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_json(
                value["badGatewayException"]
            )
        }
    elif "files" in value:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_file_part

        return {
            "files": aws_sdk_bedrock_agent_runtime.types.inline_agent_file_part.serialize_json(
                value["files"]
            )
        }
    else:
        raise SerializationError("InlineAgentResponseStream: no variant present")


def deserialize_json(data: dict) -> InlineAgentResponseStream:
    if "chunk" in data:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_payload_part

        return {
            "chunk": aws_sdk_bedrock_agent_runtime.types.inline_agent_payload_part.deserialize_json(
                data["chunk"]
            )
        }
    elif "trace" in data:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_trace_part

        return {
            "trace": aws_sdk_bedrock_agent_runtime.types.inline_agent_trace_part.deserialize_json(
                data["trace"]
            )
        }
    elif "returnControl" in data:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_return_control_payload

        return {
            "returnControl": aws_sdk_bedrock_agent_runtime.types.inline_agent_return_control_payload.deserialize_json(
                data["returnControl"]
            )
        }
    elif "internalServerException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.deserialize_json(
                data["internalServerException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agent_runtime.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    elif "resourceNotFoundException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception

        return {
            "resourceNotFoundException": aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.deserialize_json(
                data["resourceNotFoundException"]
            )
        }
    elif "serviceQuotaExceededException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception

        return {
            "serviceQuotaExceededException": aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.deserialize_json(
                data["serviceQuotaExceededException"]
            )
        }
    elif "throttlingException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_agent_runtime.errors.throttling_exception.deserialize_json(
                data["throttlingException"]
            )
        }
    elif "accessDeniedException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.deserialize_json(
                data["accessDeniedException"]
            )
        }
    elif "conflictException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.conflict_exception

        return {
            "conflictException": aws_sdk_bedrock_agent_runtime.errors.conflict_exception.deserialize_json(
                data["conflictException"]
            )
        }
    elif "dependencyFailedException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception

        return {
            "dependencyFailedException": aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_json(
                data["dependencyFailedException"]
            )
        }
    elif "badGatewayException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception

        return {
            "badGatewayException": aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.deserialize_json(
                data["badGatewayException"]
            )
        }
    elif "files" in data:
        import aws_sdk_bedrock_agent_runtime.types.inline_agent_file_part

        return {
            "files": aws_sdk_bedrock_agent_runtime.types.inline_agent_file_part.deserialize_json(
                data["files"]
            )
        }
    else:
        raise DeserializationError(
            "InlineAgentResponseStream: no recognized variant key"
        )
