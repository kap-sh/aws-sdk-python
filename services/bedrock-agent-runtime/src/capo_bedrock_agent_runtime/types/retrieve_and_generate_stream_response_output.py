"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStreamResponseOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._iter import AnyIterator
from capo_bedrock_agent_runtime._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.errors.access_denied_exception
    import capo_bedrock_agent_runtime.errors.bad_gateway_exception
    import capo_bedrock_agent_runtime.errors.conflict_exception
    import capo_bedrock_agent_runtime.errors.dependency_failed_exception
    import capo_bedrock_agent_runtime.errors.internal_server_exception
    import capo_bedrock_agent_runtime.errors.resource_not_found_exception
    import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import capo_bedrock_agent_runtime.errors.throttling_exception
    import capo_bedrock_agent_runtime.errors.validation_exception
    import capo_bedrock_agent_runtime.types.citation_event
    import capo_bedrock_agent_runtime.types.guardrail_event
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_output_event


class _RetrieveAndGenerateStreamResponseOutput_output(TypedDict, closed=True):
    output: "capo_bedrock_agent_runtime.types.retrieve_and_generate_output_event.RetrieveAndGenerateOutputEvent"


class _RetrieveAndGenerateStreamResponseOutput_citation(TypedDict, closed=True):
    citation: "capo_bedrock_agent_runtime.types.citation_event.CitationEvent"


class _RetrieveAndGenerateStreamResponseOutput_guardrail(TypedDict, closed=True):
    guardrail: "capo_bedrock_agent_runtime.types.guardrail_event.GuardrailEvent"


class _RetrieveAndGenerateStreamResponseOutput_internalServerException(
    TypedDict, closed=True
):
    internalServerException: "capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _RetrieveAndGenerateStreamResponseOutput_validationException(
    TypedDict, closed=True
):
    validationException: (
        "capo_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _RetrieveAndGenerateStreamResponseOutput_resourceNotFoundException(
    TypedDict, closed=True
):
    resourceNotFoundException: "capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _RetrieveAndGenerateStreamResponseOutput_serviceQuotaExceededException(
    TypedDict, closed=True
):
    serviceQuotaExceededException: "capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _RetrieveAndGenerateStreamResponseOutput_throttlingException(
    TypedDict, closed=True
):
    throttlingException: (
        "capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _RetrieveAndGenerateStreamResponseOutput_accessDeniedException(
    TypedDict, closed=True
):
    accessDeniedException: "capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _RetrieveAndGenerateStreamResponseOutput_conflictException(
    TypedDict, closed=True
):
    conflictException: (
        "capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _RetrieveAndGenerateStreamResponseOutput_dependencyFailedException(
    TypedDict, closed=True
):
    dependencyFailedException: "capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _RetrieveAndGenerateStreamResponseOutput_badGatewayException(
    TypedDict, closed=True
):
    badGatewayException: (
        "capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"
    )


_RetrieveAndGenerateStreamResponseOutput: TypeAlias = (
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
RetrieveAndGenerateStreamResponseOutput: TypeAlias = AnyIterator[
    _RetrieveAndGenerateStreamResponseOutput
]


def serialize_event_json(value: _RetrieveAndGenerateStreamResponseOutput) -> bytes:
    match value:
        case {"output": payload}:
            import capo_bedrock_agent_runtime.types.retrieve_and_generate_output_event

            return capo_bedrock_agent_runtime.types.retrieve_and_generate_output_event.serialize_event_json(
                payload
            )
        case {"citation": payload}:
            import capo_bedrock_agent_runtime.types.citation_event

            return capo_bedrock_agent_runtime.types.citation_event.serialize_event_json(
                payload
            )
        case {"guardrail": payload}:
            import capo_bedrock_agent_runtime.types.guardrail_event

            return (
                capo_bedrock_agent_runtime.types.guardrail_event.serialize_event_json(
                    payload
                )
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agent_runtime.errors.internal_server_exception

            return capo_bedrock_agent_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_bedrock_agent_runtime.errors.validation_exception

            return capo_bedrock_agent_runtime.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import capo_bedrock_agent_runtime.errors.resource_not_found_exception

            return capo_bedrock_agent_runtime.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception

            return capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_bedrock_agent_runtime.errors.throttling_exception

            return capo_bedrock_agent_runtime.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_bedrock_agent_runtime.errors.access_denied_exception

            return capo_bedrock_agent_runtime.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictException": payload}:
            import capo_bedrock_agent_runtime.errors.conflict_exception

            return capo_bedrock_agent_runtime.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"dependencyFailedException": payload}:
            import capo_bedrock_agent_runtime.errors.dependency_failed_exception

            return capo_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"badGatewayException": payload}:
            import capo_bedrock_agent_runtime.errors.bad_gateway_exception

            return capo_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"RetrieveAndGenerateStreamResponseOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message,
) -> _RetrieveAndGenerateStreamResponseOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "internalServerException":
                import capo_bedrock_agent_runtime.errors.internal_server_exception

                raise capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException(
                    capo_bedrock_agent_runtime.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import capo_bedrock_agent_runtime.errors.validation_exception

                raise capo_bedrock_agent_runtime.errors.validation_exception.ValidationException(
                    capo_bedrock_agent_runtime.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import capo_bedrock_agent_runtime.errors.resource_not_found_exception

                raise capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException(
                    capo_bedrock_agent_runtime.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceQuotaExceededException":
                import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception

                raise capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import capo_bedrock_agent_runtime.errors.throttling_exception

                raise capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException(
                    capo_bedrock_agent_runtime.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "accessDeniedException":
                import capo_bedrock_agent_runtime.errors.access_denied_exception

                raise capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException(
                    capo_bedrock_agent_runtime.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "conflictException":
                import capo_bedrock_agent_runtime.errors.conflict_exception

                raise capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException(
                    capo_bedrock_agent_runtime.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "dependencyFailedException":
                import capo_bedrock_agent_runtime.errors.dependency_failed_exception

                raise capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException(
                    capo_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_event_json(
                        message
                    )
                )
            case "badGatewayException":
                import capo_bedrock_agent_runtime.errors.bad_gateway_exception

                raise capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException(
                    capo_bedrock_agent_runtime.errors.bad_gateway_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"RetrieveAndGenerateStreamResponseOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "output":
            import capo_bedrock_agent_runtime.types.retrieve_and_generate_output_event

            return {
                "output": capo_bedrock_agent_runtime.types.retrieve_and_generate_output_event.deserialize_event_json(
                    message
                )
            }
        case "citation":
            import capo_bedrock_agent_runtime.types.citation_event

            return {
                "citation": capo_bedrock_agent_runtime.types.citation_event.deserialize_event_json(
                    message
                )
            }
        case "guardrail":
            import capo_bedrock_agent_runtime.types.guardrail_event

            return {
                "guardrail": capo_bedrock_agent_runtime.types.guardrail_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"RetrieveAndGenerateStreamResponseOutput: unrecognized event-type {event_type!r}"
            )
