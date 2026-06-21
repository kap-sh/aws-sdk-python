"""Generated from Smithy shape ``com.amazonaws.fsx#DataCompressionType``."""

from typing import Literal, TypeAlias, cast

DataCompressionType: TypeAlias = Literal[
    "NONE",
    "LZ4",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataCompressionType:
    return cast(DataCompressionType, data)
