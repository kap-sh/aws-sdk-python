"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TargetDbType``."""

from typing import Literal, TypeAlias, cast

TargetDbType: TypeAlias = Literal[
    "specific-database",
    "multiple-databases",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetDbType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetDbType:
    return cast(TargetDbType, data)
