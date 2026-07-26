"""Generated from Smithy shape ``com.amazonaws.greengrass#TelemetryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.configuration_sync_status
    import capo_greengrass.types.telemetry


class TelemetryConfiguration(TypedDict, closed=True):
    configuration_sync_status: NotRequired[
        "capo_greengrass.types.configuration_sync_status.ConfigurationSyncStatus"
    ]
    """Synchronization status of the device reported configuration with the desired configuration."""
    telemetry: NotRequired["capo_greengrass.types.telemetry.Telemetry"]
    """Configure telemetry to be on or off."""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfiguration) -> dict:
    out: dict = {}
    if "configuration_sync_status" in value:
        import capo_greengrass.types.configuration_sync_status

        out["ConfigurationSyncStatus"] = (
            capo_greengrass.types.configuration_sync_status.serialize_json(
                value["configuration_sync_status"]
            )
        )
    if "telemetry" in value:
        import capo_greengrass.types.telemetry

        out["Telemetry"] = capo_greengrass.types.telemetry.serialize_json(
            value["telemetry"]
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfiguration:
    out: TelemetryConfiguration = {}  # type: ignore[typeddict-item]
    if "ConfigurationSyncStatus" in data:
        import capo_greengrass.types.configuration_sync_status

        out["configuration_sync_status"] = (
            capo_greengrass.types.configuration_sync_status.deserialize_json(
                data["ConfigurationSyncStatus"]
            )
        )
    if "Telemetry" in data:
        import capo_greengrass.types.telemetry

        out["telemetry"] = capo_greengrass.types.telemetry.deserialize_json(
            data["Telemetry"]
        )
    return out
