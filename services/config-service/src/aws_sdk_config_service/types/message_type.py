"""Generated from Smithy shape ``com.amazonaws.configservice#MessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

MessageType: TypeAlias = Literal[
    "ConfigurationItemChangeNotification",
    "ConfigurationSnapshotDeliveryCompleted",
    "ScheduledNotification",
    "OversizedConfigurationItemChangeNotification",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConfigurationItemChangeNotification",
        "ConfigurationSnapshotDeliveryCompleted",
        "ScheduledNotification",
        "OversizedConfigurationItemChangeNotification",
    )
)


def serialize_aws_json_1_1(value: MessageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageType value: {data!r}")
    return cast(MessageType, data)
