"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateStepType``."""

from typing import Literal, TypeAlias, cast

CandidateStepType: TypeAlias = Literal[
    "AWS::SageMaker::TrainingJob",
    "AWS::SageMaker::TransformJob",
    "AWS::SageMaker::ProcessingJob",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateStepType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CandidateStepType:
    return cast(CandidateStepType, data)
