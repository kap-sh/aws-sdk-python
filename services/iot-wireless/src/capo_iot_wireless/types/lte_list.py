"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.lte_obj

LteList: TypeAlias = list["capo_iot_wireless.types.lte_obj.LteObj"]


# --- restJson1 ser/de ---
def serialize_json(value: LteList) -> list:
    import capo_iot_wireless.types.lte_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.lte_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> LteList:
    import capo_iot_wireless.types.lte_obj

    out: LteList = []
    for item in data:
        out.append(capo_iot_wireless.types.lte_obj.deserialize_json(item))
    return out
