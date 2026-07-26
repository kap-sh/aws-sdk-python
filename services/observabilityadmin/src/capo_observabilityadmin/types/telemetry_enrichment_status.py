"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryEnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

TelemetryEnrichmentStatus: TypeAlias = Literal[
    "Running",
    "Stopped",
    "Impaired",
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryEnrichmentStatus) -> str:
    return value


def deserialize_json(data: str) -> TelemetryEnrichmentStatus:
    return cast(TelemetryEnrichmentStatus, data)
