"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateFPorts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.applications
    import aws_sdk_iot_wireless.types.positioning


class UpdateFPorts(TypedDict):
    positioning: NotRequired["aws_sdk_iot_wireless.types.positioning.Positioning"]
    """<p>Positioning FPorts for the ClockSync, Stream, and GNSS functions.</p>"""
    applications: NotRequired["aws_sdk_iot_wireless.types.applications.Applications"]
    """<p>LoRaWAN application, which can be used for geolocation by activating positioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFPorts) -> dict:
    out: dict = {}
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.positioning

        out["Positioning"] = aws_sdk_iot_wireless.types.positioning.serialize_json(
            value["positioning"]
        )
    if "applications" in value:
        import aws_sdk_iot_wireless.types.applications

        out["Applications"] = aws_sdk_iot_wireless.types.applications.serialize_json(
            value["applications"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFPorts:
    out: UpdateFPorts = {}  # type: ignore[typeddict-item]
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.positioning

        out["positioning"] = aws_sdk_iot_wireless.types.positioning.deserialize_json(
            data["Positioning"]
        )
    if "Applications" in data:
        import aws_sdk_iot_wireless.types.applications

        out["applications"] = aws_sdk_iot_wireless.types.applications.deserialize_json(
            data["Applications"]
        )
    return out
