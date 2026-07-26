"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaNmrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wcdma_nmr_obj

WcdmaNmrList: TypeAlias = list["capo_iot_wireless.types.wcdma_nmr_obj.WcdmaNmrObj"]


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaNmrList) -> list:
    import capo_iot_wireless.types.wcdma_nmr_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.wcdma_nmr_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> WcdmaNmrList:
    import capo_iot_wireless.types.wcdma_nmr_obj

    out: WcdmaNmrList = []
    for item in data:
        out.append(capo_iot_wireless.types.wcdma_nmr_obj.deserialize_json(item))
    return out
