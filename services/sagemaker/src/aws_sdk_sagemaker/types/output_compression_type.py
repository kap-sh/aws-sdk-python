"""Generated from Smithy shape ``com.amazonaws.sagemaker#OutputCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

OutputCompressionType: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: OutputCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputCompressionType value: {data!r}")
    return cast(OutputCompressionType, data)
