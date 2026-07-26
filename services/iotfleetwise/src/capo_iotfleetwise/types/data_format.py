"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataFormat``."""

from typing import Literal, TypeAlias, cast

DataFormat: TypeAlias = Literal[
    "JSON",
    "PARQUET",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataFormat:
    return cast(DataFormat, data)
