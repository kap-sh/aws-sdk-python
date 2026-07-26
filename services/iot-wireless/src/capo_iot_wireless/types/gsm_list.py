"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.gsm_obj

GsmList: TypeAlias = list["capo_iot_wireless.types.gsm_obj.GsmObj"]


# --- restJson1 ser/de ---
def serialize_json(value: GsmList) -> list:
    import capo_iot_wireless.types.gsm_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.gsm_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> GsmList:
    import capo_iot_wireless.types.gsm_obj

    out: GsmList = []
    for item in data:
        out.append(capo_iot_wireless.types.gsm_obj.deserialize_json(item))
    return out
