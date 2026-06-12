"""Generated from Smithy shape ``com.amazonaws.sagemaker#SageMakerResourceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SageMakerResourceName: TypeAlias = Literal[
    "training-job",
    "hyperpod-cluster",
    "endpoint",
    "studio-apps",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "training-job",
        "hyperpod-cluster",
        "endpoint",
        "studio-apps",
    )
)


def serialize_aws_json_1_1(value: SageMakerResourceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SageMakerResourceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SageMakerResourceName value: {data!r}")
    return cast(SageMakerResourceName, data)
