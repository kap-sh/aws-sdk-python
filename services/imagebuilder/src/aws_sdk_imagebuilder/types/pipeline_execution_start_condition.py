"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PipelineExecutionStartCondition``."""

from typing import Literal, TypeAlias, cast

PipelineExecutionStartCondition: TypeAlias = Literal[
    "EXPRESSION_MATCH_ONLY",
    "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineExecutionStartCondition) -> str:
    return value


def deserialize_json(data: str) -> PipelineExecutionStartCondition:
    return cast(PipelineExecutionStartCondition, data)
