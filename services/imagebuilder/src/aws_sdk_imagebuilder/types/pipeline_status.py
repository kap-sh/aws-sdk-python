"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PipelineStatus``."""

from typing import Literal, TypeAlias, cast

PipelineStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> PipelineStatus:
    return cast(PipelineStatus, data)
