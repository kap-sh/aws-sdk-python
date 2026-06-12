"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaNmrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.cdma_nmr_obj

CdmaNmrList: TypeAlias = list["aws_sdk_iot_wireless.types.cdma_nmr_obj.CdmaNmrObj"]


# --- restJson1 ser/de ---
def serialize_json(value: CdmaNmrList) -> list:
    import aws_sdk_iot_wireless.types.cdma_nmr_obj

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.cdma_nmr_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> CdmaNmrList:
    import aws_sdk_iot_wireless.types.cdma_nmr_obj

    out: CdmaNmrList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.cdma_nmr_obj.deserialize_json(item))
    return out
