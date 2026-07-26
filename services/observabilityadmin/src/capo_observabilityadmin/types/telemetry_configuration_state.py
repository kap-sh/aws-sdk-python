"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryConfigurationState``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_state
    import capo_observabilityadmin.types.telemetry_type

TelemetryConfigurationState: TypeAlias = dict[
    "capo_observabilityadmin.types.telemetry_type.TelemetryType",
    "capo_observabilityadmin.types.telemetry_state.TelemetryState",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TelemetryConfigurationState) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_observabilityadmin.types.telemetry_state
        import capo_observabilityadmin.types.telemetry_type

        out[capo_observabilityadmin.types.telemetry_type.serialize_json(key)] = (
            capo_observabilityadmin.types.telemetry_state.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfigurationState:
    out: TelemetryConfigurationState = {}
    for key, value in data.items():
        import capo_observabilityadmin.types.telemetry_state
        import capo_observabilityadmin.types.telemetry_type

        out[capo_observabilityadmin.types.telemetry_type.deserialize_json(key)] = (
            capo_observabilityadmin.types.telemetry_state.deserialize_json(value)
        )
    return out
