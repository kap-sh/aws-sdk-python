"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

SnowflakeS3BackupMode: TypeAlias = Literal[
    "FailedDataOnly",
    "AllData",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FailedDataOnly",
        "AllData",
    )
)


def serialize_aws_json_1_1(value: SnowflakeS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowflakeS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnowflakeS3BackupMode value: {data!r}")
    return cast(SnowflakeS3BackupMode, data)
