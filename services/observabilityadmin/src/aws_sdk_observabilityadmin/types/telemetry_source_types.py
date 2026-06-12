"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetrySourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_source_type

TelemetrySourceTypes: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.telemetry_source_type.TelemetrySourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySourceTypes) -> list:
    import aws_sdk_observabilityadmin.types.telemetry_source_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_source_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TelemetrySourceTypes:
    import aws_sdk_observabilityadmin.types.telemetry_source_type

    out: TelemetrySourceTypes = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_source_type.deserialize_json(
                item
            )
        )
    return out
