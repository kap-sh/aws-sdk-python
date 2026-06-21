"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataSourceName``."""

from typing import Literal, TypeAlias, cast

DataSourceName: TypeAlias = Literal[
    "SalesforceGenie",
    "Snowflake",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceName:
    return cast(DataSourceName, data)
