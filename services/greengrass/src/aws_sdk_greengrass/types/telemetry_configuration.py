"""Generated from Smithy shape ``com.amazonaws.greengrass#TelemetryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.configuration_sync_status
    import aws_sdk_greengrass.types.telemetry


class TelemetryConfiguration(TypedDict):
    configuration_sync_status: NotRequired[
        "aws_sdk_greengrass.types.configuration_sync_status.ConfigurationSyncStatus"
    ]
    """Synchronization status of the device reported configuration with the desired configuration."""
    telemetry: NotRequired["aws_sdk_greengrass.types.telemetry.Telemetry"]
    """Configure telemetry to be on or off."""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfiguration) -> dict:
    out: dict = {}
    if "configuration_sync_status" in value:
        import aws_sdk_greengrass.types.configuration_sync_status

        out["ConfigurationSyncStatus"] = (
            aws_sdk_greengrass.types.configuration_sync_status.serialize_json(
                value["configuration_sync_status"]
            )
        )
    if "telemetry" in value:
        import aws_sdk_greengrass.types.telemetry

        out["Telemetry"] = aws_sdk_greengrass.types.telemetry.serialize_json(
            value["telemetry"]
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfiguration:
    out: TelemetryConfiguration = {}  # type: ignore[typeddict-item]
    if "ConfigurationSyncStatus" in data:
        import aws_sdk_greengrass.types.configuration_sync_status

        out["configuration_sync_status"] = (
            aws_sdk_greengrass.types.configuration_sync_status.deserialize_json(
                data["ConfigurationSyncStatus"]
            )
        )
    if "Telemetry" in data:
        import aws_sdk_greengrass.types.telemetry

        out["telemetry"] = aws_sdk_greengrass.types.telemetry.deserialize_json(
            data["Telemetry"]
        )
    return out
