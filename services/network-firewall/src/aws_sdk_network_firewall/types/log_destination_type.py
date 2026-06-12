"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

LogDestinationType: TypeAlias = Literal[
    "S3",
    "CloudWatchLogs",
    "KinesisDataFirehose",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "CloudWatchLogs",
        "KinesisDataFirehose",
    )
)


def serialize_aws_json_1_0(value: LogDestinationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogDestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogDestinationType value: {data!r}")
    return cast(LogDestinationType, data)
