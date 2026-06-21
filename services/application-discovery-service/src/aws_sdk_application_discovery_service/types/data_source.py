"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DataSource``."""

from typing import Literal, TypeAlias, cast

DataSource: TypeAlias = Literal["AGENT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSource:
    return cast(DataSource, data)
