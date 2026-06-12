"""Generated from Smithy shape ``com.amazonaws.sagemaker#VariantPropertyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

VariantPropertyType: TypeAlias = Literal[
    "DesiredInstanceCount",
    "DesiredWeight",
    "DataCaptureConfig",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DesiredInstanceCount",
        "DesiredWeight",
        "DataCaptureConfig",
    )
)


def serialize_aws_json_1_1(value: VariantPropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VariantPropertyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VariantPropertyType value: {data!r}")
    return cast(VariantPropertyType, data)
