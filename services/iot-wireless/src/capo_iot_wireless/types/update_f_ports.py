"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateFPorts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.applications
    import capo_iot_wireless.types.positioning


class UpdateFPorts(TypedDict, closed=True):
    positioning: NotRequired["capo_iot_wireless.types.positioning.Positioning"]
    """<p>Positioning FPorts for the ClockSync, Stream, and GNSS functions.</p>"""
    applications: NotRequired["capo_iot_wireless.types.applications.Applications"]
    """<p>LoRaWAN application, which can be used for geolocation by activating positioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFPorts) -> dict:
    out: dict = {}
    if "positioning" in value:
        import capo_iot_wireless.types.positioning

        out["Positioning"] = capo_iot_wireless.types.positioning.serialize_json(
            value["positioning"]
        )
    if "applications" in value:
        import capo_iot_wireless.types.applications

        out["Applications"] = capo_iot_wireless.types.applications.serialize_json(
            value["applications"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFPorts:
    out: UpdateFPorts = {}  # type: ignore[typeddict-item]
    if "Positioning" in data:
        import capo_iot_wireless.types.positioning

        out["positioning"] = capo_iot_wireless.types.positioning.deserialize_json(
            data["Positioning"]
        )
    if "Applications" in data:
        import capo_iot_wireless.types.applications

        out["applications"] = capo_iot_wireless.types.applications.deserialize_json(
            data["Applications"]
        )
    return out
