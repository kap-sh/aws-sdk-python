"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSDataCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OpenZFSDataCompressionType: TypeAlias = Literal[
    "NONE",
    "ZSTD",
    "LZ4",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ZSTD",
        "LZ4",
    )
)


def serialize_aws_json_1_1(value: OpenZFSDataCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSDataCompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpenZFSDataCompressionType value: {data!r}"
        )
    return cast(OpenZFSDataCompressionType, data)
