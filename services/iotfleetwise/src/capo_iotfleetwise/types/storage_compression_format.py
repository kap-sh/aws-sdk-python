"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageCompressionFormat``."""

from typing import Literal, TypeAlias, cast

StorageCompressionFormat: TypeAlias = Literal[
    "NONE",
    "GZIP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageCompressionFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageCompressionFormat:
    return cast(StorageCompressionFormat, data)
