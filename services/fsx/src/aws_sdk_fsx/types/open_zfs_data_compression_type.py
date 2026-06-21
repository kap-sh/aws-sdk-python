"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSDataCompressionType``."""

from typing import Literal, TypeAlias, cast

OpenZFSDataCompressionType: TypeAlias = Literal[
    "NONE",
    "ZSTD",
    "LZ4",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSDataCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSDataCompressionType:
    return cast(OpenZFSDataCompressionType, data)
