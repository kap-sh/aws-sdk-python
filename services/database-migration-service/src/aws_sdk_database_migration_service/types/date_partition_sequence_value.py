"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatePartitionSequenceValue``."""

from typing import Literal, TypeAlias, cast

DatePartitionSequenceValue: TypeAlias = Literal[
    "YYYYMMDD",
    "YYYYMMDDHH",
    "YYYYMM",
    "MMYYYYDD",
    "DDMMYYYY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatePartitionSequenceValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatePartitionSequenceValue:
    return cast(DatePartitionSequenceValue, data)
