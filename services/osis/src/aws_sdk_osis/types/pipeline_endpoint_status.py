"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointStatus``."""

from typing import Literal, TypeAlias, cast

PipelineEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CREATE_FAILED",
    "DELETING",
    "REVOKING",
    "REVOKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> PipelineEndpointStatus:
    return cast(PipelineEndpointStatus, data)
