"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayEventLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_event_log_option

WirelessGatewayEventLogOptionList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_gateway_event_log_option.WirelessGatewayEventLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayEventLogOptionList) -> list:
    import aws_sdk_iot_wireless.types.wireless_gateway_event_log_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.wireless_gateway_event_log_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WirelessGatewayEventLogOptionList:
    import aws_sdk_iot_wireless.types.wireless_gateway_event_log_option

    out: WirelessGatewayEventLogOptionList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.wireless_gateway_event_log_option.deserialize_json(
                item
            )
        )
    return out
