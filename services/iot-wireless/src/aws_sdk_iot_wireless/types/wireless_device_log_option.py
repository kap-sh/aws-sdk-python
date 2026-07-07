"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceLogOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.log_level
    import aws_sdk_iot_wireless.types.wireless_device_event_log_option_list
    import aws_sdk_iot_wireless.types.wireless_device_type


class WirelessDeviceLogOption(TypedDict, closed=True):
    type: "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    """<p>The wireless device type.</p>"""
    log_level: "aws_sdk_iot_wireless.types.log_level.LogLevel"
    events: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_event_log_option_list.WirelessDeviceEventLogOptionList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceLogOption) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.wireless_device_type

    out["Type"] = aws_sdk_iot_wireless.types.wireless_device_type.serialize_json(
        value["type"]
    )
    import aws_sdk_iot_wireless.types.log_level

    out["LogLevel"] = aws_sdk_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    if "events" in value:
        import aws_sdk_iot_wireless.types.wireless_device_event_log_option_list

        out["Events"] = (
            aws_sdk_iot_wireless.types.wireless_device_event_log_option_list.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> WirelessDeviceLogOption:
    out: WirelessDeviceLogOption = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_iot_wireless.types.wireless_device_type

        out["type"] = aws_sdk_iot_wireless.types.wireless_device_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("WirelessDeviceLogOption.type required")
    if "LogLevel" in data:
        import aws_sdk_iot_wireless.types.log_level

        out["log_level"] = aws_sdk_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        raise DeserializationError("WirelessDeviceLogOption.log_level required")
    if "Events" in data:
        import aws_sdk_iot_wireless.types.wireless_device_event_log_option_list

        out["events"] = (
            aws_sdk_iot_wireless.types.wireless_device_event_log_option_list.deserialize_json(
                data["Events"]
            )
        )
    return out
