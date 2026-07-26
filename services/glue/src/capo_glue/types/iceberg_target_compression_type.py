"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

IcebergTargetCompressionType: TypeAlias = Literal[
    "gzip",
    "lzo",
    "uncompressed",
    "snappy",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergTargetCompressionType:
    return cast(IcebergTargetCompressionType, data)
