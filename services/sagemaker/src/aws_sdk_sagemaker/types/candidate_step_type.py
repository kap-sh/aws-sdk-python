"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CandidateStepType: TypeAlias = Literal[
    "AWS::SageMaker::TrainingJob",
    "AWS::SageMaker::TransformJob",
    "AWS::SageMaker::ProcessingJob",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS::SageMaker::TrainingJob",
        "AWS::SageMaker::TransformJob",
        "AWS::SageMaker::ProcessingJob",
    )
)


def serialize_aws_json_1_1(value: CandidateStepType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CandidateStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CandidateStepType value: {data!r}")
    return cast(CandidateStepType, data)
