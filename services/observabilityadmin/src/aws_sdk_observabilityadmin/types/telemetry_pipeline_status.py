"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineStatus``."""

from typing import Literal, TypeAlias, cast

TelemetryPipelineStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> TelemetryPipelineStatus:
    return cast(TelemetryPipelineStatus, data)
