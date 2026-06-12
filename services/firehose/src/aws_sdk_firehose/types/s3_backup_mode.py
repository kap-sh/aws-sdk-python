"""Generated from Smithy shape ``com.amazonaws.firehose#S3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

S3BackupMode: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Disabled",
        "Enabled",
    )
)


def serialize_aws_json_1_1(value: S3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3BackupMode value: {data!r}")
    return cast(S3BackupMode, data)
