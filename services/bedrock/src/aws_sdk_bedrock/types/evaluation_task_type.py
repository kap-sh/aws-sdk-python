"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationTaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

EvaluationTaskType: TypeAlias = Literal[
    "Summarization",
    "Classification",
    "QuestionAndAnswer",
    "Generation",
    "Custom",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Summarization",
        "Classification",
        "QuestionAndAnswer",
        "Generation",
        "Custom",
    )
)


def serialize_json(value: EvaluationTaskType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationTaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationTaskType value: {data!r}")
    return cast(EvaluationTaskType, data)
