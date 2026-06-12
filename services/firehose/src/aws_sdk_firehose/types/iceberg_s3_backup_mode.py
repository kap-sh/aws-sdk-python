"""Generated from Smithy shape ``com.amazonaws.firehose#IcebergS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

IcebergS3BackupMode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: IcebergS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergS3BackupMode value: {data!r}")
    return cast(IcebergS3BackupMode, data)
