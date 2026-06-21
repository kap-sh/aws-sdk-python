"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "UPDATING",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceStatus:
    return cast(DataSourceStatus, data)
