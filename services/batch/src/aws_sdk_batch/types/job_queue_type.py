"""Generated from Smithy shape ``com.amazonaws.batch#JobQueueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

JobQueueType: TypeAlias = Literal[
    "EKS",
    "ECS",
    "ECS_FARGATE",
    "SAGEMAKER_TRAINING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EKS",
        "ECS",
        "ECS_FARGATE",
        "SAGEMAKER_TRAINING",
    )
)


def serialize_json(value: JobQueueType) -> str:
    return value


def deserialize_json(data: str) -> JobQueueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobQueueType value: {data!r}")
    return cast(JobQueueType, data)
