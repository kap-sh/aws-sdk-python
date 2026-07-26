"""Generated from Smithy shape ``com.amazonaws.batch#JobQueueType``."""

from typing import Literal, TypeAlias, cast

JobQueueType: TypeAlias = Literal[
    "EKS",
    "ECS",
    "ECS_FARGATE",
    "SAGEMAKER_TRAINING",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobQueueType) -> str:
    return value


def deserialize_json(data: str) -> JobQueueType:
    return cast(JobQueueType, data)
