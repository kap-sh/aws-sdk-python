"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OutputFormat``."""

from typing import Literal, TypeAlias, cast

OutputFormat: TypeAlias = Literal[
    "json",
    "plain",
    "w3c",
    "raw",
    "parquet",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
