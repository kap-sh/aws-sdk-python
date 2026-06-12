"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantAcceleratorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProductionVariantAcceleratorType: TypeAlias = Literal[
    "ml.eia1.medium",
    "ml.eia1.large",
    "ml.eia1.xlarge",
    "ml.eia2.medium",
    "ml.eia2.large",
    "ml.eia2.xlarge",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ml.eia1.medium",
        "ml.eia1.large",
        "ml.eia1.xlarge",
        "ml.eia2.medium",
        "ml.eia2.large",
        "ml.eia2.xlarge",
    )
)


def serialize_aws_json_1_1(value: ProductionVariantAcceleratorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductionVariantAcceleratorType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProductionVariantAcceleratorType value: {data!r}"
        )
    return cast(ProductionVariantAcceleratorType, data)
