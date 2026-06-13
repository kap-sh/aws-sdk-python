"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPromptStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
    import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
    import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
    import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
    import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
    import aws_sdk_bedrock_agent_runtime.errors.validation_exception
    import aws_sdk_bedrock_agent_runtime.types.analyze_prompt_event
    import aws_sdk_bedrock_agent_runtime.types.optimized_prompt_event


class _OptimizedPromptStream_optimizedPromptEvent(TypedDict):
    optimizedPromptEvent: "aws_sdk_bedrock_agent_runtime.types.optimized_prompt_event.OptimizedPromptEvent"


class _OptimizedPromptStream_analyzePromptEvent(TypedDict):
    analyzePromptEvent: (
        "aws_sdk_bedrock_agent_runtime.types.analyze_prompt_event.AnalyzePromptEvent"
    )


class _OptimizedPromptStream_internalServerException(TypedDict):
    internalServerException: "aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _OptimizedPromptStream_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _OptimizedPromptStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _OptimizedPromptStream_dependencyFailedException(TypedDict):
    dependencyFailedException: "aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _OptimizedPromptStream_accessDeniedException(TypedDict):
    accessDeniedException: "aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _OptimizedPromptStream_badGatewayException(TypedDict):
    badGatewayException: "aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"


OptimizedPromptStream: TypeAlias = (
    _OptimizedPromptStream_optimizedPromptEvent
    | _OptimizedPromptStream_analyzePromptEvent
    | _OptimizedPromptStream_internalServerException
    | _OptimizedPromptStream_throttlingException
    | _OptimizedPromptStream_validationException
    | _OptimizedPromptStream_dependencyFailedException
    | _OptimizedPromptStream_accessDeniedException
    | _OptimizedPromptStream_badGatewayException
)


# --- restJson1 ser/de ---
def serialize_json(value: OptimizedPromptStream) -> dict:
    if "optimizedPromptEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.optimized_prompt_event

        return {
            "optimizedPromptEvent": aws_sdk_bedrock_agent_runtime.types.optimized_prompt_event.serialize_json(
                value["optimizedPromptEvent"]
            )
        }
    elif "analyzePromptEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.analyze_prompt_event

        return {
            "analyzePromptEvent": aws_sdk_bedrock_agent_runtime.types.analyze_prompt_event.serialize_json(
                value["analyzePromptEvent"]
            )
        }
    elif "internalServerException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.serialize_json(
                value["internalServerException"]
            )
        }
    elif "throttlingException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_agent_runtime.errors.throttling_exception.serialize_json(
                value["throttlingException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agent_runtime.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    elif "dependencyFailedException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception

        return {
            "dependencyFailedException": aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_json(
                value["dependencyFailedException"]
            )
        }
    elif "accessDeniedException" in value:
        import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.serialize_json(
                value["accessDeniedException"]
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
        raise SerializationError("OptimizedPromptStream: no variant present")


def deserialize_json(data: dict) -> OptimizedPromptStream:
    if "optimizedPromptEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.optimized_prompt_event

        return {
            "optimizedPromptEvent": aws_sdk_bedrock_agent_runtime.types.optimized_prompt_event.deserialize_json(
                data["optimizedPromptEvent"]
            )
        }
    elif "analyzePromptEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.analyze_prompt_event

        return {
            "analyzePromptEvent": aws_sdk_bedrock_agent_runtime.types.analyze_prompt_event.deserialize_json(
                data["analyzePromptEvent"]
            )
        }
    elif "internalServerException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception

        return {
            "internalServerException": aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.deserialize_json(
                data["internalServerException"]
            )
        }
    elif "throttlingException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_bedrock_agent_runtime.errors.throttling_exception.deserialize_json(
                data["throttlingException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.validation_exception

        return {
            "validationException": aws_sdk_bedrock_agent_runtime.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    elif "dependencyFailedException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception

        return {
            "dependencyFailedException": aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_json(
                data["dependencyFailedException"]
            )
        }
    elif "accessDeniedException" in data:
        import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.deserialize_json(
                data["accessDeniedException"]
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
        raise DeserializationError("OptimizedPromptStream: no recognized variant key")
