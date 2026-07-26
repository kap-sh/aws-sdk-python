"""Generated from Smithy shape ``com.amazonaws.odb#SourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SourceType:
    return cast(SourceType, data)
