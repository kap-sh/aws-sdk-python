"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayLogOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.log_level
    import aws_sdk_iot_wireless.types.wireless_gateway_event_log_option_list
    import aws_sdk_iot_wireless.types.wireless_gateway_type


class WirelessGatewayLogOption(TypedDict):
    type: "aws_sdk_iot_wireless.types.wireless_gateway_type.WirelessGatewayType"
    log_level: "aws_sdk_iot_wireless.types.log_level.LogLevel"
    events: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_event_log_option_list.WirelessGatewayEventLogOptionList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayLogOption) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.wireless_gateway_type

    out["Type"] = aws_sdk_iot_wireless.types.wireless_gateway_type.serialize_json(
        value["type"]
    )
    import aws_sdk_iot_wireless.types.log_level

    out["LogLevel"] = aws_sdk_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    if "events" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_event_log_option_list

        out["Events"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_event_log_option_list.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> WirelessGatewayLogOption:
    out: WirelessGatewayLogOption = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_type

        out["type"] = aws_sdk_iot_wireless.types.wireless_gateway_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("WirelessGatewayLogOption.type required")
    if "LogLevel" in data:
        import aws_sdk_iot_wireless.types.log_level

        out["log_level"] = aws_sdk_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        raise DeserializationError("WirelessGatewayLogOption.log_level required")
    if "Events" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_event_log_option_list

        out["events"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_event_log_option_list.deserialize_json(
                data["Events"]
            )
        )
    return out
