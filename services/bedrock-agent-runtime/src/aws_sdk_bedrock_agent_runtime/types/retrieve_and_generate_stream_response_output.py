"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStreamResponseOutput``."""

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
    import aws_sdk_bedrock_agent_runtime.types.citation_event
    import aws_sdk_bedrock_agent_runtime.types.guardrail_event
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output_event


class _RetrieveAndGenerateStreamResponseOutput_output(TypedDict):
    output: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output_event.RetrieveAndGenerateOutputEvent"


class _RetrieveAndGenerateStreamResponseOutput_citation(TypedDict):
    citation: "aws_sdk_bedrock_agent_runtime.types.citation_event.CitationEvent"


class _RetrieveAndGenerateStreamResponseOutput_guardrail(TypedDict):
    guardrail: "aws_sdk_bedrock_agent_runtime.types.guardrail_event.GuardrailEvent"


class _RetrieveAndGenerateStreamResponseOutput_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _RetrieveAndGenerateStreamResponseOutput_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _RetrieveAndGenerateStreamResponseOutput_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _RetrieveAndGenerateStreamResponseOutput_serviceQuotaExceededException(TypedDict):
    serviceQuotaExceededException: "aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _RetrieveAndGenerateStreamResponseOutput_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _RetrieveAndGenerateStreamResponseOutput_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _RetrieveAndGenerateStreamResponseOutput_conflictException(TypedDict):
    conflictException: (
        "aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _RetrieveAndGenerateStreamResponseOutput_dependencyFailedException(TypedDict):
    dependencyFailedException: "aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _RetrieveAndGenerateStreamResponseOutput_badGatewayException(TypedDict):
    badGatewayException: "aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"


RetrieveAndGenerateStreamResponseOutput: TypeAlias = (
    _RetrieveAndGenerateStreamResponseOutput_output
    | _RetrieveAndGenerateStreamResponseOutput_citation
    | _RetrieveAndGenerateStreamResponseOutput_guardrail
    | _RetrieveAndGenerateStreamResponseOutput_internalServerException
    | _RetrieveAndGenerateStreamResponseOutput_validationException
    | _RetrieveAndGenerateStreamResponseOutput_resourceNotFoundException
    | _RetrieveAndGenerateStreamResponseOutput_serviceQuotaExceededException
    | _RetrieveAndGenerateStreamResponseOutput_throttlingException
    | _RetrieveAndGenerateStreamResponseOutput_accessDeniedException
    | _RetrieveAndGenerateStreamResponseOutput_conflictException
    | _RetrieveAndGenerateStreamResponseOutput_dependencyFailedException
    | _RetrieveAndGenerateStreamResponseOutput_badGatewayException
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateStreamResponseOutput) -> dict:
    if "output" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output_event

        return {
            "output": aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output_event.serialize_json(
                value["output"]
            )
        }
    elif "citation" in value:
        import aws_sdk_bedrock_agent_runtime.types.citation_event

        return {
            "citation": aws_sdk_bedrock_agent_runtime.types.citation_event.serialize_json(
                value["citation"]
            )
        }
    elif "guardrail" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_event

        return {
            "guardrail": aws_sdk_bedrock_agent_runtime.types.guardrail_event.serialize_json(
                value["guardrail"]
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
    else:
        raise SerializationError(
            "RetrieveAndGenerateStreamResponseOutput: no variant present"
        )


def deserialize_json(data: dict) -> RetrieveAndGenerateStreamResponseOutput:
    if "output" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output_event

        return {
            "output": aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output_event.deserialize_json(
                data["output"]
            )
        }
    elif "citation" in data:
        import aws_sdk_bedrock_agent_runtime.types.citation_event

        return {
            "citation": aws_sdk_bedrock_agent_runtime.types.citation_event.deserialize_json(
                data["citation"]
            )
        }
    elif "guardrail" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_event

        return {
            "guardrail": aws_sdk_bedrock_agent_runtime.types.guardrail_event.deserialize_json(
                data["guardrail"]
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
    else:
        raise DeserializationError(
            "RetrieveAndGenerateStreamResponseOutput: no recognized variant key"
        )
