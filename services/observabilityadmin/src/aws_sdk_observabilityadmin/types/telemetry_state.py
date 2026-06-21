"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryState``."""

from typing import Literal, TypeAlias, cast

TelemetryState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
    "NotApplicable",
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryState) -> str:
    return value


def deserialize_json(data: str) -> TelemetryState:
    return cast(TelemetryState, data)
