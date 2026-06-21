"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatePartitionDelimiterValue``."""

from typing import Literal, TypeAlias, cast

DatePartitionDelimiterValue: TypeAlias = Literal[
    "SLASH",
    "UNDERSCORE",
    "DASH",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatePartitionDelimiterValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatePartitionDelimiterValue:
    return cast(DatePartitionDelimiterValue, data)
