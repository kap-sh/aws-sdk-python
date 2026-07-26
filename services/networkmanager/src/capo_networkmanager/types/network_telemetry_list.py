"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkTelemetryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.network_telemetry

NetworkTelemetryList: TypeAlias = list[
    "capo_networkmanager.types.network_telemetry.NetworkTelemetry"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTelemetryList) -> list:
    import capo_networkmanager.types.network_telemetry

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.network_telemetry.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkTelemetryList:
    import capo_networkmanager.types.network_telemetry

    out: NetworkTelemetryList = []
    for item in data:
        out.append(capo_networkmanager.types.network_telemetry.deserialize_json(item))
    return out
