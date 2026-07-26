"""Generated from Smithy shape ``com.amazonaws.sagemaker#SageMakerImageName``."""

from typing import Literal, TypeAlias, cast

SageMakerImageName: TypeAlias = Literal["sagemaker_distribution",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerImageName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SageMakerImageName:
    return cast(SageMakerImageName, data)
