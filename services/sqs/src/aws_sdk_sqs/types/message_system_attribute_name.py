"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sqs.errors import DeserializationError

MessageSystemAttributeName: TypeAlias = Literal[
    "All",
    "SenderId",
    "SentTimestamp",
    "ApproximateReceiveCount",
    "ApproximateFirstReceiveTimestamp",
    "SequenceNumber",
    "MessageDeduplicationId",
    "MessageGroupId",
    "AWSTraceHeader",
    "DeadLetterQueueSourceArn",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "SenderId",
        "SentTimestamp",
        "ApproximateReceiveCount",
        "ApproximateFirstReceiveTimestamp",
        "SequenceNumber",
        "MessageDeduplicationId",
        "MessageGroupId",
        "AWSTraceHeader",
        "DeadLetterQueueSourceArn",
    )
)


def serialize_aws_json_1_0(value: MessageSystemAttributeName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MessageSystemAttributeName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MessageSystemAttributeName value: {data!r}"
        )
    return cast(MessageSystemAttributeName, data)
