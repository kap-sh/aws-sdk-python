"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore._iter import AnyIterator
from aws_sdk_bedrock_agentcore._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.errors.access_denied_exception
    import aws_sdk_bedrock_agentcore.errors.conflict_exception
    import aws_sdk_bedrock_agentcore.errors.internal_server_exception
    import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
    import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception
    import aws_sdk_bedrock_agentcore.errors.throttling_exception
    import aws_sdk_bedrock_agentcore.errors.validation_exception
    import aws_sdk_bedrock_agentcore.types.code_interpreter_result


class _CodeInterpreterStreamOutput_result(TypedDict, closed=True):
    result: (
        "aws_sdk_bedrock_agentcore.types.code_interpreter_result.CodeInterpreterResult"
    )


class _CodeInterpreterStreamOutput_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: "aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException_"


class _CodeInterpreterStreamOutput_conflictException(TypedDict, closed=True):
    conflictException: (
        "aws_sdk_bedrock_agentcore.errors.conflict_exception.ConflictException_"
    )


class _CodeInterpreterStreamOutput_internalServerException(TypedDict, closed=True):
    internalServerException: "aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _CodeInterpreterStreamOutput_resourceNotFoundException(TypedDict, closed=True):
    resourceNotFoundException: "aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException_"


class _CodeInterpreterStreamOutput_serviceQuotaExceededException(
    TypedDict, closed=True
):
    serviceQuotaExceededException: "aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _CodeInterpreterStreamOutput_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException_"
    )


class _CodeInterpreterStreamOutput_validationException(TypedDict, closed=True):
    validationException: (
        "aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException_"
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
            import aws_sdk_bedrock_agentcore.types.code_interpreter_result

            return aws_sdk_bedrock_agentcore.types.code_interpreter_result.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import aws_sdk_bedrock_agentcore.errors.access_denied_exception

            return aws_sdk_bedrock_agentcore.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictException": payload}:
            import aws_sdk_bedrock_agentcore.errors.conflict_exception

            return aws_sdk_bedrock_agentcore.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import aws_sdk_bedrock_agentcore.errors.internal_server_exception

            return aws_sdk_bedrock_agentcore.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception

            return aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception

            return aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import aws_sdk_bedrock_agentcore.errors.throttling_exception

            return aws_sdk_bedrock_agentcore.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import aws_sdk_bedrock_agentcore.errors.validation_exception

            return aws_sdk_bedrock_agentcore.errors.validation_exception.serialize_event_json(
                payload
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
                import aws_sdk_bedrock_agentcore.errors.access_denied_exception

                raise aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException(
                    aws_sdk_bedrock_agentcore.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "conflictException":
                import aws_sdk_bedrock_agentcore.errors.conflict_exception

                raise aws_sdk_bedrock_agentcore.errors.conflict_exception.ConflictException(
                    aws_sdk_bedrock_agentcore.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "internalServerException":
                import aws_sdk_bedrock_agentcore.errors.internal_server_exception

                raise aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException(
                    aws_sdk_bedrock_agentcore.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception

                raise aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException(
                    aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "serviceQuotaExceededException":
                import aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception

                raise aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import aws_sdk_bedrock_agentcore.errors.throttling_exception

                raise aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException(
                    aws_sdk_bedrock_agentcore.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import aws_sdk_bedrock_agentcore.errors.validation_exception

                raise aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException(
                    aws_sdk_bedrock_agentcore.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"CodeInterpreterStreamOutput: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "result":
            import aws_sdk_bedrock_agentcore.types.code_interpreter_result

            return {
                "result": aws_sdk_bedrock_agentcore.types.code_interpreter_result.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"CodeInterpreterStreamOutput: unrecognized event-type {event_type!r}"
            )
