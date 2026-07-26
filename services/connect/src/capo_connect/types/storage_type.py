"""Generated from Smithy shape ``com.amazonaws.connect#StorageType``."""

from typing import Literal, TypeAlias, cast

StorageType: TypeAlias = Literal[
    "S3",
    "KINESIS_VIDEO_STREAM",
    "KINESIS_STREAM",
    "KINESIS_FIREHOSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageType) -> str:
    return value


def deserialize_json(data: str) -> StorageType:
    return cast(StorageType, data)
