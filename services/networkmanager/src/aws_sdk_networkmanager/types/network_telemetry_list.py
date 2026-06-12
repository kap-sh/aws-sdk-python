"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkTelemetryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_telemetry

NetworkTelemetryList: TypeAlias = list[
    "aws_sdk_networkmanager.types.network_telemetry.NetworkTelemetry"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTelemetryList) -> list:
    import aws_sdk_networkmanager.types.network_telemetry

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.network_telemetry.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkTelemetryList:
    import aws_sdk_networkmanager.types.network_telemetry

    out: NetworkTelemetryList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.network_telemetry.deserialize_json(item)
        )
    return out
