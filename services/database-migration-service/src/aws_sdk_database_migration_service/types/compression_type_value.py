"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CompressionTypeValue``."""

from typing import Literal, TypeAlias, cast

CompressionTypeValue: TypeAlias = Literal[
    "none",
    "gzip",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionTypeValue:
    return cast(CompressionTypeValue, data)
