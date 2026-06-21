"""Generated from Smithy shape ``com.amazonaws.glue#TargetFormat``."""

from typing import Literal, TypeAlias, cast

TargetFormat: TypeAlias = Literal[
    "json",
    "csv",
    "avro",
    "orc",
    "parquet",
    "hudi",
    "delta",
    "iceberg",
    "hyper",
    "xml",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetFormat:
    return cast(TargetFormat, data)
