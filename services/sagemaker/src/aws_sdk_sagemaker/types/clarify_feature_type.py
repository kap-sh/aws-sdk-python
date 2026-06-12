"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyFeatureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClarifyFeatureType: TypeAlias = Literal[
    "numerical",
    "categorical",
    "text",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "numerical",
        "categorical",
        "text",
    )
)


def serialize_aws_json_1_1(value: ClarifyFeatureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClarifyFeatureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClarifyFeatureType value: {data!r}")
    return cast(ClarifyFeatureType, data)
