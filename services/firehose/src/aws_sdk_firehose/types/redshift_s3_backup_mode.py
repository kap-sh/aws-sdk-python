"""Generated from Smithy shape ``com.amazonaws.firehose#RedshiftS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

RedshiftS3BackupMode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: RedshiftS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedshiftS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RedshiftS3BackupMode value: {data!r}")
    return cast(RedshiftS3BackupMode, data)
