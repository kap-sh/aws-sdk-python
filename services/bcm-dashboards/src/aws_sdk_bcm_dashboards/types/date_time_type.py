"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DateTimeType``."""

from typing import Literal, TypeAlias, cast

DateTimeType: TypeAlias = Literal[
    "ABSOLUTE",
    "RELATIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DateTimeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DateTimeType:
    return cast(DateTimeType, data)
