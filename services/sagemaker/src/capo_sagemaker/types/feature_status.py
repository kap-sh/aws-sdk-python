"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureStatus``."""

from typing import Literal, TypeAlias, cast

FeatureStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureStatus:
    return cast(FeatureStatus, data)
