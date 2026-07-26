"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaNmrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.tdscdma_nmr_obj

TdscdmaNmrList: TypeAlias = list[
    "capo_iot_wireless.types.tdscdma_nmr_obj.TdscdmaNmrObj"
]


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaNmrList) -> list:
    import capo_iot_wireless.types.tdscdma_nmr_obj

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.tdscdma_nmr_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> TdscdmaNmrList:
    import capo_iot_wireless.types.tdscdma_nmr_obj

    out: TdscdmaNmrList = []
    for item in data:
        out.append(capo_iot_wireless.types.tdscdma_nmr_obj.deserialize_json(item))
    return out
