"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_kinesis.errors import DeserializationError, SerializationError

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


SubscribeToShardEventStream: TypeAlias = (
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribeToShardEventStream) -> dict:
    if "SubscribeToShardEvent" in value:
        import aws_sdk_kinesis.types.subscribe_to_shard_event

        return {
            "SubscribeToShardEvent": aws_sdk_kinesis.types.subscribe_to_shard_event.serialize_aws_json_1_1(
                value["SubscribeToShardEvent"]
            )
        }
    elif "ResourceNotFoundException" in value:
        import aws_sdk_kinesis.errors.resource_not_found_exception

        return {
            "ResourceNotFoundException": aws_sdk_kinesis.errors.resource_not_found_exception.serialize_aws_json_1_1(
                value["ResourceNotFoundException"]
            )
        }
    elif "ResourceInUseException" in value:
        import aws_sdk_kinesis.errors.resource_in_use_exception

        return {
            "ResourceInUseException": aws_sdk_kinesis.errors.resource_in_use_exception.serialize_aws_json_1_1(
                value["ResourceInUseException"]
            )
        }
    elif "KMSDisabledException" in value:
        import aws_sdk_kinesis.errors.kms_disabled_exception

        return {
            "KMSDisabledException": aws_sdk_kinesis.errors.kms_disabled_exception.serialize_aws_json_1_1(
                value["KMSDisabledException"]
            )
        }
    elif "KMSInvalidStateException" in value:
        import aws_sdk_kinesis.errors.kms_invalid_state_exception

        return {
            "KMSInvalidStateException": aws_sdk_kinesis.errors.kms_invalid_state_exception.serialize_aws_json_1_1(
                value["KMSInvalidStateException"]
            )
        }
    elif "KMSAccessDeniedException" in value:
        import aws_sdk_kinesis.errors.kms_access_denied_exception

        return {
            "KMSAccessDeniedException": aws_sdk_kinesis.errors.kms_access_denied_exception.serialize_aws_json_1_1(
                value["KMSAccessDeniedException"]
            )
        }
    elif "KMSNotFoundException" in value:
        import aws_sdk_kinesis.errors.kms_not_found_exception

        return {
            "KMSNotFoundException": aws_sdk_kinesis.errors.kms_not_found_exception.serialize_aws_json_1_1(
                value["KMSNotFoundException"]
            )
        }
    elif "KMSOptInRequired" in value:
        import aws_sdk_kinesis.errors.kms_opt_in_required

        return {
            "KMSOptInRequired": aws_sdk_kinesis.errors.kms_opt_in_required.serialize_aws_json_1_1(
                value["KMSOptInRequired"]
            )
        }
    elif "KMSThrottlingException" in value:
        import aws_sdk_kinesis.errors.kms_throttling_exception

        return {
            "KMSThrottlingException": aws_sdk_kinesis.errors.kms_throttling_exception.serialize_aws_json_1_1(
                value["KMSThrottlingException"]
            )
        }
    elif "InternalFailureException" in value:
        import aws_sdk_kinesis.errors.internal_failure_exception

        return {
            "InternalFailureException": aws_sdk_kinesis.errors.internal_failure_exception.serialize_aws_json_1_1(
                value["InternalFailureException"]
            )
        }
    else:
        raise SerializationError("SubscribeToShardEventStream: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SubscribeToShardEventStream:
    if "SubscribeToShardEvent" in data:
        import aws_sdk_kinesis.types.subscribe_to_shard_event

        return {
            "SubscribeToShardEvent": aws_sdk_kinesis.types.subscribe_to_shard_event.deserialize_aws_json_1_1(
                data["SubscribeToShardEvent"]
            )
        }
    elif "ResourceNotFoundException" in data:
        import aws_sdk_kinesis.errors.resource_not_found_exception

        return {
            "ResourceNotFoundException": aws_sdk_kinesis.errors.resource_not_found_exception.deserialize_aws_json_1_1(
                data["ResourceNotFoundException"]
            )
        }
    elif "ResourceInUseException" in data:
        import aws_sdk_kinesis.errors.resource_in_use_exception

        return {
            "ResourceInUseException": aws_sdk_kinesis.errors.resource_in_use_exception.deserialize_aws_json_1_1(
                data["ResourceInUseException"]
            )
        }
    elif "KMSDisabledException" in data:
        import aws_sdk_kinesis.errors.kms_disabled_exception

        return {
            "KMSDisabledException": aws_sdk_kinesis.errors.kms_disabled_exception.deserialize_aws_json_1_1(
                data["KMSDisabledException"]
            )
        }
    elif "KMSInvalidStateException" in data:
        import aws_sdk_kinesis.errors.kms_invalid_state_exception

        return {
            "KMSInvalidStateException": aws_sdk_kinesis.errors.kms_invalid_state_exception.deserialize_aws_json_1_1(
                data["KMSInvalidStateException"]
            )
        }
    elif "KMSAccessDeniedException" in data:
        import aws_sdk_kinesis.errors.kms_access_denied_exception

        return {
            "KMSAccessDeniedException": aws_sdk_kinesis.errors.kms_access_denied_exception.deserialize_aws_json_1_1(
                data["KMSAccessDeniedException"]
            )
        }
    elif "KMSNotFoundException" in data:
        import aws_sdk_kinesis.errors.kms_not_found_exception

        return {
            "KMSNotFoundException": aws_sdk_kinesis.errors.kms_not_found_exception.deserialize_aws_json_1_1(
                data["KMSNotFoundException"]
            )
        }
    elif "KMSOptInRequired" in data:
        import aws_sdk_kinesis.errors.kms_opt_in_required

        return {
            "KMSOptInRequired": aws_sdk_kinesis.errors.kms_opt_in_required.deserialize_aws_json_1_1(
                data["KMSOptInRequired"]
            )
        }
    elif "KMSThrottlingException" in data:
        import aws_sdk_kinesis.errors.kms_throttling_exception

        return {
            "KMSThrottlingException": aws_sdk_kinesis.errors.kms_throttling_exception.deserialize_aws_json_1_1(
                data["KMSThrottlingException"]
            )
        }
    elif "InternalFailureException" in data:
        import aws_sdk_kinesis.errors.internal_failure_exception

        return {
            "InternalFailureException": aws_sdk_kinesis.errors.internal_failure_exception.deserialize_aws_json_1_1(
                data["InternalFailureException"]
            )
        }
    else:
        raise DeserializationError(
            "SubscribeToShardEventStream: no recognized variant key"
        )
