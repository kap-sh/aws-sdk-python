"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.cdma_obj

CdmaList: TypeAlias = list["capo_iot_wireless.types.cdma_obj.CdmaObj"]


# --- restJson1 ser/de ---
def serialize_json(value: CdmaList) -> list:
    import capo_iot_wireless.types.cdma_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.cdma_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> CdmaList:
    import capo_iot_wireless.types.cdma_obj

    out: CdmaList = []
    for item in data:
        out.append(capo_iot_wireless.types.cdma_obj.deserialize_json(item))
    return out
