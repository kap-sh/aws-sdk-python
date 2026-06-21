"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_kinesis._iter import AnyIterator
from aws_sdk_kinesis._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_kinesis.errors.internal_failure_exception
    import aws_sdk_kinesis.errors.kms_access_denied_exception
    import aws_sdk_kinesis.errors.kms_disabled_exception
    import aws_sdk_kinesis.errors.kms_invalid_state_exception
    import aws_sdk_kinesis.errors.kms_not_found_exception
    import aws_sdk_kinesis.errors.kms_opt_in_required
    import aws_sdk_kinesis.errors.kms_throttling_exception
    import aws_sdk_kinesis.errors.resource_in_use_exception
    import aws_sdk_kinesis.errors.resource_not_found_exception
    import aws_sdk_kinesis.types.subscribe_to_shard_event


class _SubscribeToShardEventStream_SubscribeToShardEvent(TypedDict):
    SubscribeToShardEvent: (
        "aws_sdk_kinesis.types.subscribe_to_shard_event.SubscribeToShardEvent"
    )


class _SubscribeToShardEventStream_ResourceNotFoundException(TypedDict):
    ResourceNotFoundException: (
        "aws_sdk_kinesis.errors.resource_not_found_exception.ResourceNotFoundException_"
    )


class _SubscribeToShardEventStream_ResourceInUseException(TypedDict):
    ResourceInUseException: (
        "aws_sdk_kinesis.errors.resource_in_use_exception.ResourceInUseException_"
    )


class _SubscribeToShardEventStream_KMSDisabledException(TypedDict):
    KMSDisabledException: (
        "aws_sdk_kinesis.errors.kms_disabled_exception.KMSDisabledException_"
    )


class _SubscribeToShardEventStream_KMSInvalidStateException(TypedDict):
    KMSInvalidStateException: (
        "aws_sdk_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException_"
    )


class _SubscribeToShardEventStream_KMSAccessDeniedException(TypedDict):
    KMSAccessDeniedException: (
        "aws_sdk_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException_"
    )


class _SubscribeToShardEventStream_KMSNotFoundException(TypedDict):
    KMSNotFoundException: (
        "aws_sdk_kinesis.errors.kms_not_found_exception.KMSNotFoundException_"
    )


class _SubscribeToShardEventStream_KMSOptInRequired(TypedDict):
    KMSOptInRequired: "aws_sdk_kinesis.errors.kms_opt_in_required.KMSOptInRequired_"


class _SubscribeToShardEventStream_KMSThrottlingException(TypedDict):
    KMSThrottlingException: (
        "aws_sdk_kinesis.errors.kms_throttling_exception.KMSThrottlingException_"
    )


class _SubscribeToShardEventStream_InternalFailureException(TypedDict):
    InternalFailureException: (
        "aws_sdk_kinesis.errors.internal_failure_exception.InternalFailureException_"
    )


_SubscribeToShardEventStream: TypeAlias = (
    _SubscribeToShardEventStream_SubscribeToShardEvent
    | _SubscribeToShardEventStream_ResourceNotFoundException
    | _SubscribeToShardEventStream_ResourceInUseException
    | _SubscribeToShardEventStream_KMSDisabledException
    | _SubscribeToShardEventStream_KMSInvalidStateException
    | _SubscribeToShardEventStream_KMSAccessDeniedException
    | _SubscribeToShardEventStream_KMSNotFoundException
    | _SubscribeToShardEventStream_KMSOptInRequired
    | _SubscribeToShardEventStream_KMSThrottlingException
    | _SubscribeToShardEventStream_InternalFailureException
)
SubscribeToShardEventStream: TypeAlias = AnyIterator[_SubscribeToShardEventStream]


def serialize_event_aws_json_1_1(value: _SubscribeToShardEventStream) -> bytes:
    match value:
        case {"SubscribeToShardEvent": payload}:
            import aws_sdk_kinesis.types.subscribe_to_shard_event

            return aws_sdk_kinesis.types.subscribe_to_shard_event.serialize_event_aws_json_1_1(
                payload
            )
        case {"ResourceNotFoundException": payload}:
            import aws_sdk_kinesis.errors.resource_not_found_exception

            return aws_sdk_kinesis.errors.resource_not_found_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"ResourceInUseException": payload}:
            import aws_sdk_kinesis.errors.resource_in_use_exception

            return aws_sdk_kinesis.errors.resource_in_use_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSDisabledException": payload}:
            import aws_sdk_kinesis.errors.kms_disabled_exception

            return aws_sdk_kinesis.errors.kms_disabled_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSInvalidStateException": payload}:
            import aws_sdk_kinesis.errors.kms_invalid_state_exception

            return aws_sdk_kinesis.errors.kms_invalid_state_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSAccessDeniedException": payload}:
            import aws_sdk_kinesis.errors.kms_access_denied_exception

            return aws_sdk_kinesis.errors.kms_access_denied_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSNotFoundException": payload}:
            import aws_sdk_kinesis.errors.kms_not_found_exception

            return aws_sdk_kinesis.errors.kms_not_found_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSOptInRequired": payload}:
            import aws_sdk_kinesis.errors.kms_opt_in_required

            return (
                aws_sdk_kinesis.errors.kms_opt_in_required.serialize_event_aws_json_1_1(
                    payload
                )
            )
        case {"KMSThrottlingException": payload}:
            import aws_sdk_kinesis.errors.kms_throttling_exception

            return aws_sdk_kinesis.errors.kms_throttling_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"InternalFailureException": payload}:
            import aws_sdk_kinesis.errors.internal_failure_exception

            return aws_sdk_kinesis.errors.internal_failure_exception.serialize_event_aws_json_1_1(
                payload
            )
        case _:
            raise ValueError(
                f"SubscribeToShardEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_1(message: Message) -> _SubscribeToShardEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "ResourceNotFoundException":
                import aws_sdk_kinesis.errors.resource_not_found_exception

                raise aws_sdk_kinesis.errors.resource_not_found_exception.ResourceNotFoundException(
                    aws_sdk_kinesis.errors.resource_not_found_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "ResourceInUseException":
                import aws_sdk_kinesis.errors.resource_in_use_exception

                raise aws_sdk_kinesis.errors.resource_in_use_exception.ResourceInUseException(
                    aws_sdk_kinesis.errors.resource_in_use_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "KMSDisabledException":
                import aws_sdk_kinesis.errors.kms_disabled_exception

                raise aws_sdk_kinesis.errors.kms_disabled_exception.KMSDisabledException(
                    aws_sdk_kinesis.errors.kms_disabled_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "KMSInvalidStateException":
                import aws_sdk_kinesis.errors.kms_invalid_state_exception

                raise aws_sdk_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException(
                    aws_sdk_kinesis.errors.kms_invalid_state_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "KMSAccessDeniedException":
                import aws_sdk_kinesis.errors.kms_access_denied_exception

                raise aws_sdk_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException(
                    aws_sdk_kinesis.errors.kms_access_denied_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "KMSNotFoundException":
                import aws_sdk_kinesis.errors.kms_not_found_exception

                raise aws_sdk_kinesis.errors.kms_not_found_exception.KMSNotFoundException(
                    aws_sdk_kinesis.errors.kms_not_found_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "KMSOptInRequired":
                import aws_sdk_kinesis.errors.kms_opt_in_required

                raise aws_sdk_kinesis.errors.kms_opt_in_required.KMSOptInRequired(
                    aws_sdk_kinesis.errors.kms_opt_in_required.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "KMSThrottlingException":
                import aws_sdk_kinesis.errors.kms_throttling_exception

                raise aws_sdk_kinesis.errors.kms_throttling_exception.KMSThrottlingException(
                    aws_sdk_kinesis.errors.kms_throttling_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "InternalFailureException":
                import aws_sdk_kinesis.errors.internal_failure_exception

                raise aws_sdk_kinesis.errors.internal_failure_exception.InternalFailureException(
                    aws_sdk_kinesis.errors.internal_failure_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
        raise ValueError(
            f"SubscribeToShardEventStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "SubscribeToShardEvent":
            import aws_sdk_kinesis.types.subscribe_to_shard_event

            return {
                "SubscribeToShardEvent": aws_sdk_kinesis.types.subscribe_to_shard_event.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case _:
            raise ValueError(
                f"SubscribeToShardEventStream: unrecognized event-type {event_type!r}"
            )
