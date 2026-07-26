"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateThingRuntimeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.telemetry_configuration_update


class UpdateThingRuntimeConfigurationRequest(TypedDict, closed=True):
    telemetry_configuration: NotRequired[
        "capo_greengrass.types.telemetry_configuration_update.TelemetryConfigurationUpdate"
    ]
    """Configuration for telemetry service."""
    thing_name: "capo_greengrass.types.__string.__string"
    """The thing name."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingRuntimeConfigurationRequest) -> dict:
    out: dict = {}
    if "telemetry_configuration" in value:
        import capo_greengrass.types.telemetry_configuration_update

        out["TelemetryConfiguration"] = (
            capo_greengrass.types.telemetry_configuration_update.serialize_json(
                value["telemetry_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateThingRuntimeConfigurationRequest:
    out: UpdateThingRuntimeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TelemetryConfiguration" in data:
        import capo_greengrass.types.telemetry_configuration_update

        out["telemetry_configuration"] = (
            capo_greengrass.types.telemetry_configuration_update.deserialize_json(
                data["TelemetryConfiguration"]
            )
        )
    return out
