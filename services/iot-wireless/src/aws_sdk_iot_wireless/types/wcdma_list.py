"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wcdma_obj

WcdmaList: TypeAlias = list["aws_sdk_iot_wireless.types.wcdma_obj.WcdmaObj"]


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaList) -> list:
    import aws_sdk_iot_wireless.types.wcdma_obj

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.wcdma_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> WcdmaList:
    import aws_sdk_iot_wireless.types.wcdma_obj

    out: WcdmaList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.wcdma_obj.deserialize_json(item))
    return out
