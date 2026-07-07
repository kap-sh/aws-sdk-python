"""Generated from Smithy shape ``com.amazonaws.iotwireless#TraceContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.log_level
    import aws_sdk_iot_wireless.types.multicast_frame_info
    import aws_sdk_iot_wireless.types.wireless_device_frame_info


class TraceContent(TypedDict, closed=True):
    wireless_device_frame_info: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_frame_info.WirelessDeviceFrameInfo"
    ]
    log_level: NotRequired["aws_sdk_iot_wireless.types.log_level.LogLevel"]
    multicast_frame_info: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_frame_info.MulticastFrameInfo"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TraceContent) -> dict:
    out: dict = {}
    if "wireless_device_frame_info" in value:
        import aws_sdk_iot_wireless.types.wireless_device_frame_info

        out["WirelessDeviceFrameInfo"] = (
            aws_sdk_iot_wireless.types.wireless_device_frame_info.serialize_json(
                value["wireless_device_frame_info"]
            )
        )
    if "log_level" in value:
        import aws_sdk_iot_wireless.types.log_level

        out["LogLevel"] = aws_sdk_iot_wireless.types.log_level.serialize_json(
            value["log_level"]
        )
    if "multicast_frame_info" in value:
        import aws_sdk_iot_wireless.types.multicast_frame_info

        out["MulticastFrameInfo"] = (
            aws_sdk_iot_wireless.types.multicast_frame_info.serialize_json(
                value["multicast_frame_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> TraceContent:
    out: TraceContent = {}  # type: ignore[typeddict-item]
    if "WirelessDeviceFrameInfo" in data:
        import aws_sdk_iot_wireless.types.wireless_device_frame_info

        out["wireless_device_frame_info"] = (
            aws_sdk_iot_wireless.types.wireless_device_frame_info.deserialize_json(
                data["WirelessDeviceFrameInfo"]
            )
        )
    if "LogLevel" in data:
        import aws_sdk_iot_wireless.types.log_level

        out["log_level"] = aws_sdk_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    if "MulticastFrameInfo" in data:
        import aws_sdk_iot_wireless.types.multicast_frame_info

        out["multicast_frame_info"] = (
            aws_sdk_iot_wireless.types.multicast_frame_info.deserialize_json(
                data["MulticastFrameInfo"]
            )
        )
    return out
