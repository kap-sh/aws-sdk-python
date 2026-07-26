"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ParquetVersionValue``."""

from typing import Literal, TypeAlias, cast

ParquetVersionValue: TypeAlias = Literal[
    "parquet-1-0",
    "parquet-2-0",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParquetVersionValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetVersionValue:
    return cast(ParquetVersionValue, data)
