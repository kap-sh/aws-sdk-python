"""Generated from Smithy shape ``com.amazonaws.connect#StorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

StorageType: TypeAlias = Literal[
    "S3",
    "KINESIS_VIDEO_STREAM",
    "KINESIS_STREAM",
    "KINESIS_FIREHOSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "KINESIS_VIDEO_STREAM",
        "KINESIS_STREAM",
        "KINESIS_FIREHOSE",
    )
)


def serialize_json(value: StorageType) -> str:
    return value


def deserialize_json(data: str) -> StorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageType value: {data!r}")
    return cast(StorageType, data)
