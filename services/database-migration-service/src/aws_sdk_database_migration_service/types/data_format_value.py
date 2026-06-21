"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataFormatValue``."""

from typing import Literal, TypeAlias, cast

DataFormatValue: TypeAlias = Literal[
    "csv",
    "parquet",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataFormatValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataFormatValue:
    return cast(DataFormatValue, data)
