"""Generated from Smithy shape ``com.amazonaws.firehose#OrcCompression``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

OrcCompression: TypeAlias = Literal[
    "NONE",
    "ZLIB",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ZLIB",
        "SNAPPY",
    )
)


def serialize_aws_json_1_1(value: OrcCompression) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrcCompression:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrcCompression value: {data!r}")
    return cast(OrcCompression, data)
