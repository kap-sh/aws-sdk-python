"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError, SerializationError

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


ResponseStream: TypeAlias = (
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


# --- restJson1 ser/de ---
def serialize_json(value: ResponseStream) -> dict:
    if "trace" in value:
        import aws_sdk_iotsitewise.types.trace

        return {"trace": aws_sdk_iotsitewise.types.trace.serialize_json(value["trace"])}
    elif "output" in value:
        import aws_sdk_iotsitewise.types.invocation_output

        return {
            "output": aws_sdk_iotsitewise.types.invocation_output.serialize_json(
                value["output"]
            )
        }
    elif "accessDeniedException" in value:
        import aws_sdk_iotsitewise.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_iotsitewise.errors.access_denied_exception.serialize_json(
                value["accessDeniedException"]
            )
        }
    elif "conflictingOperationException" in value:
        import aws_sdk_iotsitewise.errors.conflicting_operation_exception

        return {
            "conflictingOperationException": aws_sdk_iotsitewise.errors.conflicting_operation_exception.serialize_json(
                value["conflictingOperationException"]
            )
        }
    elif "internalFailureException" in value:
        import aws_sdk_iotsitewise.errors.internal_failure_exception

        return {
            "internalFailureException": aws_sdk_iotsitewise.errors.internal_failure_exception.serialize_json(
                value["internalFailureException"]
            )
        }
    elif "invalidRequestException" in value:
        import aws_sdk_iotsitewise.errors.invalid_request_exception

        return {
            "invalidRequestException": aws_sdk_iotsitewise.errors.invalid_request_exception.serialize_json(
                value["invalidRequestException"]
            )
        }
    elif "limitExceededException" in value:
        import aws_sdk_iotsitewise.errors.limit_exceeded_exception

        return {
            "limitExceededException": aws_sdk_iotsitewise.errors.limit_exceeded_exception.serialize_json(
                value["limitExceededException"]
            )
        }
    elif "resourceNotFoundException" in value:
        import aws_sdk_iotsitewise.errors.resource_not_found_exception

        return {
            "resourceNotFoundException": aws_sdk_iotsitewise.errors.resource_not_found_exception.serialize_json(
                value["resourceNotFoundException"]
            )
        }
    elif "throttlingException" in value:
        import aws_sdk_iotsitewise.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_iotsitewise.errors.throttling_exception.serialize_json(
                value["throttlingException"]
            )
        }
    else:
        raise SerializationError("ResponseStream: no variant present")


def deserialize_json(data: dict) -> ResponseStream:
    if "trace" in data:
        import aws_sdk_iotsitewise.types.trace

        return {
            "trace": aws_sdk_iotsitewise.types.trace.deserialize_json(data["trace"])
        }
    elif "output" in data:
        import aws_sdk_iotsitewise.types.invocation_output

        return {
            "output": aws_sdk_iotsitewise.types.invocation_output.deserialize_json(
                data["output"]
            )
        }
    elif "accessDeniedException" in data:
        import aws_sdk_iotsitewise.errors.access_denied_exception

        return {
            "accessDeniedException": aws_sdk_iotsitewise.errors.access_denied_exception.deserialize_json(
                data["accessDeniedException"]
            )
        }
    elif "conflictingOperationException" in data:
        import aws_sdk_iotsitewise.errors.conflicting_operation_exception

        return {
            "conflictingOperationException": aws_sdk_iotsitewise.errors.conflicting_operation_exception.deserialize_json(
                data["conflictingOperationException"]
            )
        }
    elif "internalFailureException" in data:
        import aws_sdk_iotsitewise.errors.internal_failure_exception

        return {
            "internalFailureException": aws_sdk_iotsitewise.errors.internal_failure_exception.deserialize_json(
                data["internalFailureException"]
            )
        }
    elif "invalidRequestException" in data:
        import aws_sdk_iotsitewise.errors.invalid_request_exception

        return {
            "invalidRequestException": aws_sdk_iotsitewise.errors.invalid_request_exception.deserialize_json(
                data["invalidRequestException"]
            )
        }
    elif "limitExceededException" in data:
        import aws_sdk_iotsitewise.errors.limit_exceeded_exception

        return {
            "limitExceededException": aws_sdk_iotsitewise.errors.limit_exceeded_exception.deserialize_json(
                data["limitExceededException"]
            )
        }
    elif "resourceNotFoundException" in data:
        import aws_sdk_iotsitewise.errors.resource_not_found_exception

        return {
            "resourceNotFoundException": aws_sdk_iotsitewise.errors.resource_not_found_exception.deserialize_json(
                data["resourceNotFoundException"]
            )
        }
    elif "throttlingException" in data:
        import aws_sdk_iotsitewise.errors.throttling_exception

        return {
            "throttlingException": aws_sdk_iotsitewise.errors.throttling_exception.deserialize_json(
                data["throttlingException"]
            )
        }
    else:
        raise DeserializationError("ResponseStream: no recognized variant key")
