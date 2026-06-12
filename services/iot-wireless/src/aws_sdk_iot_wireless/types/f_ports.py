"""Generated from Smithy shape ``com.amazonaws.iotwireless#FPorts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.applications
    import aws_sdk_iot_wireless.types.f_port
    import aws_sdk_iot_wireless.types.positioning


class FPorts(TypedDict):
    fuota: NotRequired["aws_sdk_iot_wireless.types.f_port.FPort"]
    multicast: NotRequired["aws_sdk_iot_wireless.types.f_port.FPort"]
    clock_sync: NotRequired["aws_sdk_iot_wireless.types.f_port.FPort"]
    positioning: NotRequired["aws_sdk_iot_wireless.types.positioning.Positioning"]
    """<p>FPort values for the GNSS, stream, and ClockSync functions of the positioning information.</p>"""
    applications: NotRequired["aws_sdk_iot_wireless.types.applications.Applications"]
    """<p>Optional LoRaWAN application information, which can be used for geolocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FPorts) -> dict:
    out: dict = {}
    if "fuota" in value:
        out["Fuota"] = value["fuota"]
    if "multicast" in value:
        out["Multicast"] = value["multicast"]
    if "clock_sync" in value:
        out["ClockSync"] = value["clock_sync"]
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


def deserialize_json(data: dict) -> FPorts:
    out: FPorts = {}  # type: ignore[typeddict-item]
    if "Fuota" in data:
        out["fuota"] = data["Fuota"]
    if "Multicast" in data:
        out["multicast"] = data["Multicast"]
    if "ClockSync" in data:
        out["clock_sync"] = data["ClockSync"]
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
