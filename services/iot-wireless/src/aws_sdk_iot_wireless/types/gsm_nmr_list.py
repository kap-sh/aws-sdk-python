"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmNmrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.gsm_nmr_obj

GsmNmrList: TypeAlias = list["aws_sdk_iot_wireless.types.gsm_nmr_obj.GsmNmrObj"]


# --- restJson1 ser/de ---
def serialize_json(value: GsmNmrList) -> list:
    import aws_sdk_iot_wireless.types.gsm_nmr_obj

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.gsm_nmr_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> GsmNmrList:
    import aws_sdk_iot_wireless.types.gsm_nmr_obj

    out: GsmNmrList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.gsm_nmr_obj.deserialize_json(item))
    return out
