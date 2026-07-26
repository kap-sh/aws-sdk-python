"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteNmrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.lte_nmr_obj

LteNmrList: TypeAlias = list["capo_iot_wireless.types.lte_nmr_obj.LteNmrObj"]


# --- restJson1 ser/de ---
def serialize_json(value: LteNmrList) -> list:
    import capo_iot_wireless.types.lte_nmr_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.lte_nmr_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> LteNmrList:
    import capo_iot_wireless.types.lte_nmr_obj

    out: LteNmrList = []
    for item in data:
        out.append(capo_iot_wireless.types.lte_nmr_obj.deserialize_json(item))
    return out
