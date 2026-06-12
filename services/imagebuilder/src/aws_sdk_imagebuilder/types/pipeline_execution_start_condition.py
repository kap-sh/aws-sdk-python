"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PipelineExecutionStartCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

PipelineExecutionStartCondition: TypeAlias = Literal[
    "EXPRESSION_MATCH_ONLY",
    "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPRESSION_MATCH_ONLY",
        "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE",
    )
)


def serialize_json(value: PipelineExecutionStartCondition) -> str:
    return value


def deserialize_json(data: str) -> PipelineExecutionStartCondition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PipelineExecutionStartCondition value: {data!r}"
        )
    return cast(PipelineExecutionStartCondition, data)
