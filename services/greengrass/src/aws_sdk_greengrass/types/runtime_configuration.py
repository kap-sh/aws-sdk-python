"""Generated from Smithy shape ``com.amazonaws.greengrass#RuntimeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.telemetry_configuration


class RuntimeConfiguration(TypedDict, closed=True):
    telemetry_configuration: NotRequired[
        "aws_sdk_greengrass.types.telemetry_configuration.TelemetryConfiguration"
    ]
    """Configuration for telemetry service."""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeConfiguration) -> dict:
    out: dict = {}
    if "telemetry_configuration" in value:
        import aws_sdk_greengrass.types.telemetry_configuration

        out["TelemetryConfiguration"] = (
            aws_sdk_greengrass.types.telemetry_configuration.serialize_json(
                value["telemetry_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeConfiguration:
    out: RuntimeConfiguration = {}  # type: ignore[typeddict-item]
    if "TelemetryConfiguration" in data:
        import aws_sdk_greengrass.types.telemetry_configuration

        out["telemetry_configuration"] = (
            aws_sdk_greengrass.types.telemetry_configuration.deserialize_json(
                data["TelemetryConfiguration"]
            )
        )
    return out
