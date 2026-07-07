"""Generated from Smithy shape ``com.amazonaws.greengrass#TelemetryConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.telemetry


class TelemetryConfigurationUpdate(TypedDict, closed=True):
    telemetry: NotRequired["aws_sdk_greengrass.types.telemetry.Telemetry"]
    """Configure telemetry to be on or off."""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfigurationUpdate) -> dict:
    out: dict = {}
    if "telemetry" in value:
        import aws_sdk_greengrass.types.telemetry

        out["Telemetry"] = aws_sdk_greengrass.types.telemetry.serialize_json(
            value["telemetry"]
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfigurationUpdate:
    out: TelemetryConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "Telemetry" in data:
        import aws_sdk_greengrass.types.telemetry

        out["telemetry"] = aws_sdk_greengrass.types.telemetry.deserialize_json(
            data["Telemetry"]
        )
    return out
