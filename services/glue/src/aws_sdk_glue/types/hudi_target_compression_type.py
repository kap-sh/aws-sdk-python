"""Generated from Smithy shape ``com.amazonaws.glue#HudiTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

HudiTargetCompressionType: TypeAlias = Literal[
    "gzip",
    "lzo",
    "uncompressed",
    "snappy",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "gzip",
        "lzo",
        "uncompressed",
        "snappy",
    )
)


def serialize_aws_json_1_1(value: HudiTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HudiTargetCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HudiTargetCompressionType value: {data!r}")
    return cast(HudiTargetCompressionType, data)
