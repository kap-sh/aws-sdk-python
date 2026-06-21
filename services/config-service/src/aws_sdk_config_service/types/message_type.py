"""Generated from Smithy shape ``com.amazonaws.configservice#MessageType``."""

from typing import Literal, TypeAlias, cast

MessageType: TypeAlias = Literal[
    "ConfigurationItemChangeNotification",
    "ConfigurationSnapshotDeliveryCompleted",
    "ScheduledNotification",
    "OversizedConfigurationItemChangeNotification",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MessageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageType:
    return cast(MessageType, data)
