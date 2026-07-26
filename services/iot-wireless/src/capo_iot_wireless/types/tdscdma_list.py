"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.tdscdma_obj

TdscdmaList: TypeAlias = list["capo_iot_wireless.types.tdscdma_obj.TdscdmaObj"]


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaList) -> list:
    import capo_iot_wireless.types.tdscdma_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.tdscdma_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> TdscdmaList:
    import capo_iot_wireless.types.tdscdma_obj

    out: TdscdmaList = []
    for item in data:
        out.append(capo_iot_wireless.types.tdscdma_obj.deserialize_json(item))
    return out
