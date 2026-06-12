"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayTaskDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.update_wireless_gateway_task_entry

WirelessGatewayTaskDefinitionList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.update_wireless_gateway_task_entry.UpdateWirelessGatewayTaskEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayTaskDefinitionList) -> list:
    import aws_sdk_iot_wireless.types.update_wireless_gateway_task_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.update_wireless_gateway_task_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WirelessGatewayTaskDefinitionList:
    import aws_sdk_iot_wireless.types.update_wireless_gateway_task_entry

    out: WirelessGatewayTaskDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.update_wireless_gateway_task_entry.deserialize_json(
                item
            )
        )
    return out
