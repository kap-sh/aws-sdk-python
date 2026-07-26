"""Generated from Smithy shape ``com.amazonaws.iotwireless#TraceContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.log_level
    import capo_iot_wireless.types.multicast_frame_info
    import capo_iot_wireless.types.wireless_device_frame_info


class TraceContent(TypedDict, closed=True):
    wireless_device_frame_info: NotRequired[
        "capo_iot_wireless.types.wireless_device_frame_info.WirelessDeviceFrameInfo"
    ]
    log_level: NotRequired["capo_iot_wireless.types.log_level.LogLevel"]
    multicast_frame_info: NotRequired[
        "capo_iot_wireless.types.multicast_frame_info.MulticastFrameInfo"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TraceContent) -> dict:
    out: dict = {}
    if "wireless_device_frame_info" in value:
        import capo_iot_wireless.types.wireless_device_frame_info

        out["WirelessDeviceFrameInfo"] = (
            capo_iot_wireless.types.wireless_device_frame_info.serialize_json(
                value["wireless_device_frame_info"]
            )
        )
    if "log_level" in value:
        import capo_iot_wireless.types.log_level

        out["LogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
            value["log_level"]
        )
    if "multicast_frame_info" in value:
        import capo_iot_wireless.types.multicast_frame_info

        out["MulticastFrameInfo"] = (
            capo_iot_wireless.types.multicast_frame_info.serialize_json(
                value["multicast_frame_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> TraceContent:
    out: TraceContent = {}  # type: ignore[typeddict-item]
    if "WirelessDeviceFrameInfo" in data:
        import capo_iot_wireless.types.wireless_device_frame_info

        out["wireless_device_frame_info"] = (
            capo_iot_wireless.types.wireless_device_frame_info.deserialize_json(
                data["WirelessDeviceFrameInfo"]
            )
        )
    if "LogLevel" in data:
        import capo_iot_wireless.types.log_level

        out["log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    if "MulticastFrameInfo" in data:
        import capo_iot_wireless.types.multicast_frame_info

        out["multicast_frame_info"] = (
            capo_iot_wireless.types.multicast_frame_info.deserialize_json(
                data["MulticastFrameInfo"]
            )
        )
    return out
