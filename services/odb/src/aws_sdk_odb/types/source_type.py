"""Generated from Smithy shape ``com.amazonaws.odb#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "NONE",
    "DATABASE",
    "BACKUP_FROM_ID",
    "BACKUP_FROM_TIMESTAMP",
    "CROSS_REGION_DATAGUARD",
    "CROSS_REGION_DISASTER_RECOVERY",
    "CLONE_TO_REFRESHABLE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DATABASE",
        "BACKUP_FROM_ID",
        "BACKUP_FROM_TIMESTAMP",
        "CROSS_REGION_DATAGUARD",
        "CROSS_REGION_DISASTER_RECOVERY",
        "CLONE_TO_REFRESHABLE",
    )
)


def serialize_aws_json_1_0(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
