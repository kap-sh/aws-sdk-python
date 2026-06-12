"""Generated from Smithy shape ``com.amazonaws.glue#DeltaTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DeltaTargetCompressionType: TypeAlias = Literal[
    "uncompressed",
    "snappy",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "uncompressed",
        "snappy",
    )
)


def serialize_aws_json_1_1(value: DeltaTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeltaTargetCompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeltaTargetCompressionType value: {data!r}"
        )
    return cast(DeltaTargetCompressionType, data)
