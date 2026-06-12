"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageCompressionFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

StorageCompressionFormat: TypeAlias = Literal[
    "NONE",
    "GZIP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "GZIP",
    )
)


def serialize_aws_json_1_0(value: StorageCompressionFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageCompressionFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageCompressionFormat value: {data!r}")
    return cast(StorageCompressionFormat, data)
