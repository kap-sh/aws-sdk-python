"""Generated from Smithy shape ``com.amazonaws.sagemaker#SageMakerResourceName``."""

from typing import Literal, TypeAlias, cast

SageMakerResourceName: TypeAlias = Literal[
    "training-job",
    "hyperpod-cluster",
    "endpoint",
    "studio-apps",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerResourceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SageMakerResourceName:
    return cast(SageMakerResourceName, data)
