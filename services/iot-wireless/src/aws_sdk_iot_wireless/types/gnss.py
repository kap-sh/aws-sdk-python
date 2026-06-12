"""Generated from Smithy shape ``com.amazonaws.iotwireless#Gnss``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.assist_position
    import aws_sdk_iot_wireless.types.capture_time_accuracy
    import aws_sdk_iot_wireless.types.coordinate
    import aws_sdk_iot_wireless.types.gnss_nav
    import aws_sdk_iot_wireless.types.gpst
    import aws_sdk_iot_wireless.types.use2_d_solver


class Gnss(TypedDict):
    payload: "aws_sdk_iot_wireless.types.gnss_nav.GnssNav"
    """<p>Payload that contains the GNSS scan result, or NAV message, in hexadecimal notation.</p>"""
    capture_time: NotRequired["aws_sdk_iot_wireless.types.gpst.GPST"]
    """<p>Optional parameter that gives an estimate of the time when the GNSS scan information is taken, in seconds GPS time (GPST). If capture time is not specified, the local server time is used.</p>"""
    capture_time_accuracy: NotRequired[
        "aws_sdk_iot_wireless.types.capture_time_accuracy.CaptureTimeAccuracy"
    ]
    """<p>Optional value that gives the capture time estimate accuracy, in seconds. If capture time accuracy is not specified, default value of 300 is used.</p>"""
    assist_position: NotRequired[
        "aws_sdk_iot_wireless.types.assist_position.AssistPosition"
    ]
    """<p>Optional assistance position information, specified using latitude and longitude values in degrees. The coordinates are inside the WGS84 reference frame.</p>"""
    assist_altitude: NotRequired["aws_sdk_iot_wireless.types.coordinate.Coordinate"]
    """<p>Optional assistance altitude, which is the altitude of the device at capture time, specified in meters above the WGS84 reference ellipsoid.</p>"""
    use2_d_solver: "aws_sdk_iot_wireless.types.use2_d_solver.Use2DSolver"
    """<p>Optional parameter that forces 2D solve, which modifies the positioning algorithm to a 2D solution problem. When this parameter is specified, the assistance altitude should have an accuracy of at least 10 meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Gnss) -> dict:
    out: dict = {}
    out["Payload"] = value["payload"]
    if "capture_time" in value:
        out["CaptureTime"] = value["capture_time"]
    if "capture_time_accuracy" in value:
        out["CaptureTimeAccuracy"] = value["capture_time_accuracy"]
    if "assist_position" in value:
        import aws_sdk_iot_wireless.types.assist_position

        out["AssistPosition"] = (
            aws_sdk_iot_wireless.types.assist_position.serialize_json(
                value["assist_position"]
            )
        )
    if "assist_altitude" in value:
        out["AssistAltitude"] = value["assist_altitude"]
    out["Use2DSolver"] = value.get("use2_d_solver", False)
    return out


def deserialize_json(data: dict) -> Gnss:
    out: Gnss = {}  # type: ignore[typeddict-item]
    if "Payload" in data:
        out["payload"] = data["Payload"]
    else:
        raise DeserializationError("Gnss.payload required")
    if "CaptureTime" in data:
        out["capture_time"] = data["CaptureTime"]
    if "CaptureTimeAccuracy" in data:
        out["capture_time_accuracy"] = data["CaptureTimeAccuracy"]
    if "AssistPosition" in data:
        import aws_sdk_iot_wireless.types.assist_position

        out["assist_position"] = (
            aws_sdk_iot_wireless.types.assist_position.deserialize_json(
                data["AssistPosition"]
            )
        )
    if "AssistAltitude" in data:
        out["assist_altitude"] = data["AssistAltitude"]
    if "Use2DSolver" in data:
        out["use2_d_solver"] = data["Use2DSolver"]
    else:
        out["use2_d_solver"] = False
    return out
