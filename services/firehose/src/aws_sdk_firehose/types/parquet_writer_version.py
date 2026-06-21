"""Generated from Smithy shape ``com.amazonaws.firehose#ParquetWriterVersion``."""

from typing import Literal, TypeAlias, cast

ParquetWriterVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParquetWriterVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetWriterVersion:
    return cast(ParquetWriterVersion, data)
