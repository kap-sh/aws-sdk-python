"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentCapacitySizeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceComponentCapacitySizeType: TypeAlias = Literal[
    "COPY_COUNT",
    "CAPACITY_PERCENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COPY_COUNT",
        "CAPACITY_PERCENT",
    )
)


def serialize_aws_json_1_1(value: InferenceComponentCapacitySizeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentCapacitySizeType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InferenceComponentCapacitySizeType value: {data!r}"
        )
    return cast(InferenceComponentCapacitySizeType, data)
