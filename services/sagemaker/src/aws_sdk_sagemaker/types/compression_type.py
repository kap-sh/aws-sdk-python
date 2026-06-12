"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CompressionType: TypeAlias = Literal[
    "None",
    "Gzip",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Gzip",
    )
)


def serialize_aws_json_1_1(value: CompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionType value: {data!r}")
    return cast(CompressionType, data)
