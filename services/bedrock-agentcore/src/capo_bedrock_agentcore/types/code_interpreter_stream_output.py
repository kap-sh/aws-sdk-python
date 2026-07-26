"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore._iter import AnyIterator
from capo_bedrock_agentcore._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_bedrock_agentcore.errors.access_denied_exception
    import capo_bedrock_agentcore.errors.conflict_exception
    import capo_bedrock_agentcore.errors.internal_server_exception
    import capo_bedrock_agentcore.errors.resource_not_found_exception
    import capo_bedrock_agentcore.errors.service_quota_exceeded_exception
    import capo_bedrock_agentcore.errors.throttling_exception
    import capo_bedrock_agentcore.errors.validation_exception
    import capo_bedrock_agentcore.types.code_interpreter_result


class _CodeInterpreterStreamOutput_result(TypedDict, closed=True):
    result: "capo_bedrock_agentcore.types.code_interpreter_result.CodeInterpreterResult"


class _CodeInterpreterStreamOutput_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: (
        "capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException_"
    )


class _CodeInterpreterStreamOutput_conflictException(TypedDict, closed=True):
    conflictException: (
        "capo_bedrock_agentcore.errors.conflict_exception.ConflictException_"
    )


class _CodeInterpreterStreamOutput_internalServerException(TypedDict, closed=True):
    internalServerException: "capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _CodeInterpreterStreamOutput_resourceNotFoundException(TypedDict, closed=True):
    resourceNotFoundException: "capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException_"


class _CodeInterpreterStreamOutput_serviceQuotaExceededException(
    TypedDict, closed=True
):
    serviceQuotaExceededException: "capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _CodeInterpreterStreamOutput_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException_"
    )


class _CodeInterpreterStreamOutput_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


_CodeInterpreterStreamOutput: TypeAlias = (
    _CodeInterpreterStreamOutput_result
    | _CodeInterpreterStreamOutput_accessDeniedException
    | _CodeInterpreterStreamOutput_conflictException
    | _CodeInterpreterStreamOutput_internalServerException
    | _CodeInterpreterStreamOutput_resourceNotFoundException
    | _CodeInterpreterStreamOutput_serviceQuotaExceededException
    | _CodeInterpreterStreamOutput_throttlingException
    | _CodeInterpreterStreamOutput_validationException
)
CodeInterpreterStreamOutput: TypeAlias = AnyIterator[_CodeInterpreterStreamOutput]


def serialize_event_json(value: _CodeInterpreterStreamOutput) -> bytes:
    match value:
        case {"result": payload}:
            import capo_bedrock_agentcore.types.code_interpreter_result

            return capo_bedrock_agentcore.types.code_interpreter_result.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_bedrock_agentcore.errors.access_denied_exception

            return capo_bedrock_agentcore.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictException": payload}:
            import capo_bedrock_agentcore.errors.conflict_exception

            return (
                capo_bedrock_agentcore.errors.conflict_exception.serialize_event_json(
                    payload
                )
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agentcore.errors.internal_server_exception

            return capo_bedrock_agentcore.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import capo_bedrock_agentcore.errors.resource_not_found_exception

            return capo_bedrock_agentcore.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import capo_bedrock_agentcore.errors.service_quota_exceeded_exception

            return capo_bedrock_agentcore.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_bedrock_agentcore.errors.throttling_exception

            return (
                capo_bedrock_agentcore.errors.throttling_exception.serialize_event_json(
                    payload
                )
            )
        case {"validationException": payload}:
            import capo_bedrock_agentcore.errors.validation_exception

            return (
                capo_bedrock_agentcore.errors.validation_exception.serialize_event_json(
                    payload
                )
            )
        case _:
            raise ValueError(
                f"CodeInterpreterStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _CodeInterpreterStreamOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "accessDeniedException":
                import capo_bedrock_agentcore.errors.access_denied_exception

                raise capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException(
                    capo_bedrock_agentcore.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "conflictException":
                import capo_bedrock_agentcore.errors.conflict_exception

                raise capo_bedrock_agentcore.errors.conflict_exception.ConflictException(
                    capo_bedrock_agentcore.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "internalServerException":
                import capo_bedrock_agentcore.errors.internal_server_exception

                raise capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException(
                    capo_bedrock_agentcore.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import capo_bedrock_agentcore.errors.resource_not_found_exception

                raise capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException(
                    capo_bedrock_agentcore.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceQuotaExceededException":
                import capo_bedrock_agentcore.errors.service_quota_exceeded_exception

                raise capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    capo_bedrock_agentcore.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import capo_bedrock_agentcore.errors.throttling_exception

                raise capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException(
                    capo_bedrock_agentcore.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import capo_bedrock_agentcore.errors.validation_exception

                raise capo_bedrock_agentcore.errors.validation_exception.ValidationException(
                    capo_bedrock_agentcore.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"CodeInterpreterStreamOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "result":
            import capo_bedrock_agentcore.types.code_interpreter_result

            return {
                "result": capo_bedrock_agentcore.types.code_interpreter_result.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"CodeInterpreterStreamOutput: unrecognized event-type {event_type!r}"
            )
