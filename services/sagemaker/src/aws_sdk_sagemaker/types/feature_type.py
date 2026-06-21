"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureType``."""

from typing import Literal, TypeAlias, cast

FeatureType: TypeAlias = Literal[
    "Integral",
    "Fractional",
    "String",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureType:
    return cast(FeatureType, data)
