"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkDeviceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.battery_level
    import capo_iot_wireless.types.device_state
    import capo_iot_wireless.types.event
    import capo_iot_wireless.types.integer


class SidewalkDeviceMetadata(TypedDict, closed=True):
    rssi: NotRequired["capo_iot_wireless.types.integer.Integer"]
    """<p>The RSSI value.</p>"""
    battery_level: NotRequired["capo_iot_wireless.types.battery_level.BatteryLevel"]
    """<p>Sidewalk device battery level.</p>"""
    event: NotRequired["capo_iot_wireless.types.event.Event"]
    """<p>Sidewalk device status notification.</p>"""
    device_state: NotRequired["capo_iot_wireless.types.device_state.DeviceState"]
    """<p>Device state defines the device status of sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkDeviceMetadata) -> dict:
    out: dict = {}
    if "rssi" in value:
        out["Rssi"] = value["rssi"]
    if "battery_level" in value:
        import capo_iot_wireless.types.battery_level

        out["BatteryLevel"] = capo_iot_wireless.types.battery_level.serialize_json(
            value["battery_level"]
        )
    if "event" in value:
        import capo_iot_wireless.types.event

        out["Event"] = capo_iot_wireless.types.event.serialize_json(value["event"])
    if "device_state" in value:
        import capo_iot_wireless.types.device_state

        out["DeviceState"] = capo_iot_wireless.types.device_state.serialize_json(
            value["device_state"]
        )
    return out


def deserialize_json(data: dict) -> SidewalkDeviceMetadata:
    out: SidewalkDeviceMetadata = {}  # type: ignore[typeddict-item]
    if "Rssi" in data:
        out["rssi"] = data["Rssi"]
    if "BatteryLevel" in data:
        import capo_iot_wireless.types.battery_level

        out["battery_level"] = capo_iot_wireless.types.battery_level.deserialize_json(
            data["BatteryLevel"]
        )
    if "Event" in data:
        import capo_iot_wireless.types.event

        out["event"] = capo_iot_wireless.types.event.deserialize_json(data["Event"])
    if "DeviceState" in data:
        import capo_iot_wireless.types.device_state

        out["device_state"] = capo_iot_wireless.types.device_state.deserialize_json(
            data["DeviceState"]
        )
    return out
