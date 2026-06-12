"""Generated from Smithy shape ``com.amazonaws.sqs#QueueAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sqs.errors import DeserializationError

QueueAttributeName: TypeAlias = Literal[
    "All",
    "Policy",
    "VisibilityTimeout",
    "MaximumMessageSize",
    "MessageRetentionPeriod",
    "ApproximateNumberOfMessages",
    "ApproximateNumberOfMessagesNotVisible",
    "CreatedTimestamp",
    "LastModifiedTimestamp",
    "QueueArn",
    "ApproximateNumberOfMessagesDelayed",
    "DelaySeconds",
    "ReceiveMessageWaitTimeSeconds",
    "RedrivePolicy",
    "FifoQueue",
    "ContentBasedDeduplication",
    "KmsMasterKeyId",
    "KmsDataKeyReusePeriodSeconds",
    "DeduplicationScope",
    "FifoThroughputLimit",
    "RedriveAllowPolicy",
    "SqsManagedSseEnabled",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Policy",
        "VisibilityTimeout",
        "MaximumMessageSize",
        "MessageRetentionPeriod",
        "ApproximateNumberOfMessages",
        "ApproximateNumberOfMessagesNotVisible",
        "CreatedTimestamp",
        "LastModifiedTimestamp",
        "QueueArn",
        "ApproximateNumberOfMessagesDelayed",
        "DelaySeconds",
        "ReceiveMessageWaitTimeSeconds",
        "RedrivePolicy",
        "FifoQueue",
        "ContentBasedDeduplication",
        "KmsMasterKeyId",
        "KmsDataKeyReusePeriodSeconds",
        "DeduplicationScope",
        "FifoThroughputLimit",
        "RedriveAllowPolicy",
        "SqsManagedSseEnabled",
    )
)


def serialize_aws_json_1_0(value: QueueAttributeName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueueAttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueAttributeName value: {data!r}")
    return cast(QueueAttributeName, data)
