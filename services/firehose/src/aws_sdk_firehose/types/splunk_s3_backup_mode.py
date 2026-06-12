"""Generated from Smithy shape ``com.amazonaws.firehose#SplunkS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

SplunkS3BackupMode: TypeAlias = Literal[
    "FailedEventsOnly",
    "AllEvents",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FailedEventsOnly",
        "AllEvents",
    )
)


def serialize_aws_json_1_1(value: SplunkS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SplunkS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SplunkS3BackupMode value: {data!r}")
    return cast(SplunkS3BackupMode, data)
