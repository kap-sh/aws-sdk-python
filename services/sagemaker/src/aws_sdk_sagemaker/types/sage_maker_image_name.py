"""Generated from Smithy shape ``com.amazonaws.sagemaker#SageMakerImageName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SageMakerImageName: TypeAlias = Literal["sagemaker_distribution",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("sagemaker_distribution",))


def serialize_aws_json_1_1(value: SageMakerImageName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SageMakerImageName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SageMakerImageName value: {data!r}")
    return cast(SageMakerImageName, data)
