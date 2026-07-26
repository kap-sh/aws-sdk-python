"""Generated from Smithy shape ``com.amazonaws.iotwireless#GatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.gateway_list_item

GatewayList: TypeAlias = list[
    "capo_iot_wireless.types.gateway_list_item.GatewayListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayList) -> list:
    import capo_iot_wireless.types.gateway_list_item

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.gateway_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> GatewayList:
    import capo_iot_wireless.types.gateway_list_item

    out: GatewayList = []
    for item in data:
        out.append(capo_iot_wireless.types.gateway_list_item.deserialize_json(item))
    return out
