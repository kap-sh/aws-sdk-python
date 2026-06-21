"""Generated from Smithy shape ``com.amazonaws.medialive#PipelineId``."""

from typing import Literal, TypeAlias, cast

"""Pipeline ID"""
PipelineId: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineId) -> str:
    return value


def deserialize_json(data: str) -> PipelineId:
    return cast(PipelineId, data)
