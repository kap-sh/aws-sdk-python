"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetrySourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_source_type

TelemetrySourceTypes: TypeAlias = list[
    "capo_observabilityadmin.types.telemetry_source_type.TelemetrySourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySourceTypes) -> list:
    import capo_observabilityadmin.types.telemetry_source_type

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.telemetry_source_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TelemetrySourceTypes:
    import capo_observabilityadmin.types.telemetry_source_type

    out: TelemetrySourceTypes = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.telemetry_source_type.deserialize_json(item)
        )
    return out
