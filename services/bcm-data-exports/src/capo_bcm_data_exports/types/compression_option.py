"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#CompressionOption``."""

from typing import Literal, TypeAlias, cast

CompressionOption: TypeAlias = Literal[
    "GZIP",
    "PARQUET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionOption:
    return cast(CompressionOption, data)
