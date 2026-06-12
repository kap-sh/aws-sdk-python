"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateThingRuntimeConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.telemetry_configuration_update


class UpdateThingRuntimeConfigurationRequest(TypedDict):
    telemetry_configuration: NotRequired[
        "aws_sdk_greengrass.types.telemetry_configuration_update.TelemetryConfigurationUpdate"
    ]
    """Configuration for telemetry service."""
    thing_name: "aws_sdk_greengrass.types.__string.__string"
    """The thing name."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingRuntimeConfigurationRequest) -> dict:
    out: dict = {}
    if "telemetry_configuration" in value:
        import aws_sdk_greengrass.types.telemetry_configuration_update

        out["TelemetryConfiguration"] = (
            aws_sdk_greengrass.types.telemetry_configuration_update.serialize_json(
                value["telemetry_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateThingRuntimeConfigurationRequest:
    out: UpdateThingRuntimeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TelemetryConfiguration" in data:
        import aws_sdk_greengrass.types.telemetry_configuration_update

        out["telemetry_configuration"] = (
            aws_sdk_greengrass.types.telemetry_configuration_update.deserialize_json(
                data["TelemetryConfiguration"]
            )
        )
    return out
