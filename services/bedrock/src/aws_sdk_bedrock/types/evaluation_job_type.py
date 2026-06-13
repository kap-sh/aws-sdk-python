"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

EvaluationJobType: TypeAlias = Literal[
    "Human",
    "Automated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Human",
        "Automated",
    )
)


def serialize_json(value: EvaluationJobType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationJobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationJobType value: {data!r}")
    return cast(EvaluationJobType, data)
