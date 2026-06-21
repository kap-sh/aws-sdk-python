"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iotsitewise._iter import AnyIterator
from aws_sdk_iotsitewise._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.errors.access_denied_exception
    import aws_sdk_iotsitewise.errors.conflicting_operation_exception
    import aws_sdk_iotsitewise.errors.internal_failure_exception
    import aws_sdk_iotsitewise.errors.invalid_request_exception
    import aws_sdk_iotsitewise.errors.limit_exceeded_exception
    import aws_sdk_iotsitewise.errors.resource_not_found_exception
    import aws_sdk_iotsitewise.errors.throttling_exception
    import aws_sdk_iotsitewise.types.invocation_output
    import aws_sdk_iotsitewise.types.trace


class _ResponseStream_trace(TypedDict):
    trace: "aws_sdk_iotsitewise.types.trace.Trace"


class _ResponseStream_output(TypedDict):
    output: "aws_sdk_iotsitewise.types.invocation_output.InvocationOutput"


class _ResponseStream_accessDeniedException(TypedDict):
    accessDeniedException: (
        "aws_sdk_iotsitewise.errors.access_denied_exception.AccessDeniedException_"
    )


class _ResponseStream_conflictingOperationException(TypedDict):
    conflictingOperationException: "aws_sdk_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException_"


class _ResponseStream_internalFailureException(TypedDict):
    internalFailureException: "aws_sdk_iotsitewise.errors.internal_failure_exception.InternalFailureException_"


class _ResponseStream_invalidRequestException(TypedDict):
    invalidRequestException: (
        "aws_sdk_iotsitewise.errors.invalid_request_exception.InvalidRequestException_"
    )


class _ResponseStream_limitExceededException(TypedDict):
    limitExceededException: (
        "aws_sdk_iotsitewise.errors.limit_exceeded_exception.LimitExceededException_"
    )


class _ResponseStream_resourceNotFoundException(TypedDict):
    resourceNotFoundException: "aws_sdk_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException_"


class _ResponseStream_throttlingException(TypedDict):
    throttlingException: (
        "aws_sdk_iotsitewise.errors.throttling_exception.ThrottlingException_"
    )


_ResponseStream: TypeAlias = (
    _ResponseStream_trace
    | _ResponseStream_output
    | _ResponseStream_accessDeniedException
    | _ResponseStream_conflictingOperationException
    | _ResponseStream_internalFailureException
    | _ResponseStream_invalidRequestException
    | _ResponseStream_limitExceededException
    | _ResponseStream_resourceNotFoundException
    | _ResponseStream_throttlingException
)
ResponseStream: TypeAlias = AnyIterator[_ResponseStream]


def serialize_event_json(value: _ResponseStream) -> bytes:
    match value:
        case {"trace": payload}:
            import aws_sdk_iotsitewise.types.trace

            return aws_sdk_iotsitewise.types.trace.serialize_event_json(payload)
        case {"output": payload}:
            import aws_sdk_iotsitewise.types.invocation_output

            return aws_sdk_iotsitewise.types.invocation_output.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import aws_sdk_iotsitewise.errors.access_denied_exception

            return (
                aws_sdk_iotsitewise.errors.access_denied_exception.serialize_event_json(
                    payload
                )
            )
        case {"conflictingOperationException": payload}:
            import aws_sdk_iotsitewise.errors.conflicting_operation_exception

            return aws_sdk_iotsitewise.errors.conflicting_operation_exception.serialize_event_json(
                payload
            )
        case {"internalFailureException": payload}:
            import aws_sdk_iotsitewise.errors.internal_failure_exception

            return aws_sdk_iotsitewise.errors.internal_failure_exception.serialize_event_json(
                payload
            )
        case {"invalidRequestException": payload}:
            import aws_sdk_iotsitewise.errors.invalid_request_exception

            return aws_sdk_iotsitewise.errors.invalid_request_exception.serialize_event_json(
                payload
            )
        case {"limitExceededException": payload}:
            import aws_sdk_iotsitewise.errors.limit_exceeded_exception

            return aws_sdk_iotsitewise.errors.limit_exceeded_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import aws_sdk_iotsitewise.errors.resource_not_found_exception

            return aws_sdk_iotsitewise.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import aws_sdk_iotsitewise.errors.throttling_exception

            return aws_sdk_iotsitewise.errors.throttling_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "accessDeniedException":
                import aws_sdk_iotsitewise.errors.access_denied_exception

                raise aws_sdk_iotsitewise.errors.access_denied_exception.AccessDeniedException(
                    aws_sdk_iotsitewise.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "conflictingOperationException":
                import aws_sdk_iotsitewise.errors.conflicting_operation_exception

                raise aws_sdk_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException(
                    aws_sdk_iotsitewise.errors.conflicting_operation_exception.deserialize_event_json(
                        message
                    )
                )
            case "internalFailureException":
                import aws_sdk_iotsitewise.errors.internal_failure_exception

                raise aws_sdk_iotsitewise.errors.internal_failure_exception.InternalFailureException(
                    aws_sdk_iotsitewise.errors.internal_failure_exception.deserialize_event_json(
                        message
                    )
                )
            case "invalidRequestException":
                import aws_sdk_iotsitewise.errors.invalid_request_exception

                raise aws_sdk_iotsitewise.errors.invalid_request_exception.InvalidRequestException(
                    aws_sdk_iotsitewise.errors.invalid_request_exception.deserialize_event_json(
                        message
                    )
                )
            case "limitExceededException":
                import aws_sdk_iotsitewise.errors.limit_exceeded_exception

                raise aws_sdk_iotsitewise.errors.limit_exceeded_exception.LimitExceededException(
                    aws_sdk_iotsitewise.errors.limit_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "resourceNotFoundException":
                import aws_sdk_iotsitewise.errors.resource_not_found_exception

                raise aws_sdk_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException(
                    aws_sdk_iotsitewise.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "throttlingException":
                import aws_sdk_iotsitewise.errors.throttling_exception

                raise aws_sdk_iotsitewise.errors.throttling_exception.ThrottlingException(
                    aws_sdk_iotsitewise.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(f"ResponseStream: unrecognized error-type {error_type!r}")
    event_type = headers.get(":event-type")
    match event_type:
        case "trace":
            import aws_sdk_iotsitewise.types.trace

            return {
                "trace": aws_sdk_iotsitewise.types.trace.deserialize_event_json(message)
            }
        case "output":
            import aws_sdk_iotsitewise.types.invocation_output

            return {
                "output": aws_sdk_iotsitewise.types.invocation_output.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
