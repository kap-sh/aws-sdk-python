"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_configuration

TelemetryConfigurations: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.telemetry_configuration.TelemetryConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfigurations) -> list:
    import aws_sdk_observabilityadmin.types.telemetry_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TelemetryConfigurations:
    import aws_sdk_observabilityadmin.types.telemetry_configuration

    out: TelemetryConfigurations = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_configuration.deserialize_json(
                item
            )
        )
    return out
