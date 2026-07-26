"""Generated from Smithy shape ``com.amazonaws.sagemaker#VariantPropertyType``."""

from typing import Literal, TypeAlias, cast

VariantPropertyType: TypeAlias = Literal[
    "DesiredInstanceCount",
    "DesiredWeight",
    "DataCaptureConfig",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariantPropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VariantPropertyType:
    return cast(VariantPropertyType, data)
