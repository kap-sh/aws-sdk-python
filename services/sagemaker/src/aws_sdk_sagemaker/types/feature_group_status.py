"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupStatus``."""

from typing import Literal, TypeAlias, cast

FeatureGroupStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "CreateFailed",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureGroupStatus:
    return cast(FeatureGroupStatus, data)
