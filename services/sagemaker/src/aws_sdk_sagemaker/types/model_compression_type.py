"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCompressionType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ModelCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCompressionType value: {data!r}")
    return cast(ModelCompressionType, data)
