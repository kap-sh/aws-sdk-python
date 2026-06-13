"""Generated from Smithy shape ``com.amazonaws.location#DeviceState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.cell_signals
    import aws_sdk_location.types.id
    import aws_sdk_location.types.position
    import aws_sdk_location.types.positional_accuracy
    import aws_sdk_location.types.timestamp
    import aws_sdk_location.types.wi_fi_access_point_list


class DeviceState(TypedDict):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The device identifier.</p>"""
    sample_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device's position was determined. Uses <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601 </a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    position: "aws_sdk_location.types.position.Position"
    """<p>The last known device position.</p>"""
    accuracy: NotRequired[
        "aws_sdk_location.types.positional_accuracy.PositionalAccuracy"
    ]
    ipv4_address: NotRequired["str"]
    """<p>The device's Ipv4 address.</p>"""
    wi_fi_access_points: NotRequired[
        "aws_sdk_location.types.wi_fi_access_point_list.WiFiAccessPointList"
    ]
    """<p>The Wi-Fi access points the device is using.</p>"""
    cell_signals: NotRequired["aws_sdk_location.types.cell_signals.CellSignals"]
    """<p>The cellular network infrastructure that the device is connected to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceState) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.timestamp

    out["SampleTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import aws_sdk_location.types.position

    out["Position"] = aws_sdk_location.types.position.serialize_json(value["position"])
    if "accuracy" in value:
        import aws_sdk_location.types.positional_accuracy

        out["Accuracy"] = aws_sdk_location.types.positional_accuracy.serialize_json(
            value["accuracy"]
        )
    if "ipv4_address" in value:
        out["Ipv4Address"] = value["ipv4_address"]
    if "wi_fi_access_points" in value:
        import aws_sdk_location.types.wi_fi_access_point_list

        out["WiFiAccessPoints"] = (
            aws_sdk_location.types.wi_fi_access_point_list.serialize_json(
                value["wi_fi_access_points"]
            )
        )
    if "cell_signals" in value:
        import aws_sdk_location.types.cell_signals

        out["CellSignals"] = aws_sdk_location.types.cell_signals.serialize_json(
            value["cell_signals"]
        )
    return out


def deserialize_json(data: dict) -> DeviceState:
    out: DeviceState = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("DeviceState.device_id required")
    if "SampleTime" in data:
        import aws_sdk_location.types.timestamp

        out["sample_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("DeviceState.sample_time required")
    if "Position" in data:
        import aws_sdk_location.types.position

        out["position"] = aws_sdk_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("DeviceState.position required")
    if "Accuracy" in data:
        import aws_sdk_location.types.positional_accuracy

        out["accuracy"] = aws_sdk_location.types.positional_accuracy.deserialize_json(
            data["Accuracy"]
        )
    if "Ipv4Address" in data:
        out["ipv4_address"] = data["Ipv4Address"]
    if "WiFiAccessPoints" in data:
        import aws_sdk_location.types.wi_fi_access_point_list

        out["wi_fi_access_points"] = (
            aws_sdk_location.types.wi_fi_access_point_list.deserialize_json(
                data["WiFiAccessPoints"]
            )
        )
    if "CellSignals" in data:
        import aws_sdk_location.types.cell_signals

        out["cell_signals"] = aws_sdk_location.types.cell_signals.deserialize_json(
            data["CellSignals"]
        )
    return out
