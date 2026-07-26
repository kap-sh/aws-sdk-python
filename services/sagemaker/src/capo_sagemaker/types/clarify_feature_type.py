"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyFeatureType``."""

from typing import Literal, TypeAlias, cast

ClarifyFeatureType: TypeAlias = Literal[
    "numerical",
    "categorical",
    "text",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyFeatureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClarifyFeatureType:
    return cast(ClarifyFeatureType, data)
