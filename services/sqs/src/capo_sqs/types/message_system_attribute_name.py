"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: MessageSystemAttributeName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MessageSystemAttributeName:
    return cast(MessageSystemAttributeName, data)
