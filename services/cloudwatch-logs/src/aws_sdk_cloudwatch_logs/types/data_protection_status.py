"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataProtectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

DataProtectionStatus: TypeAlias = Literal[
    "ACTIVATED",
    "DELETED",
    "ARCHIVED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATED",
        "DELETED",
        "ARCHIVED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: DataProtectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataProtectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataProtectionStatus value: {data!r}")
    return cast(DataProtectionStatus, data)
