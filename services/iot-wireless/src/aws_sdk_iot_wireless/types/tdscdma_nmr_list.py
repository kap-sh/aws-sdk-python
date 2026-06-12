"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaNmrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.tdscdma_nmr_obj

TdscdmaNmrList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.tdscdma_nmr_obj.TdscdmaNmrObj"
]


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaNmrList) -> list:
    import aws_sdk_iot_wireless.types.tdscdma_nmr_obj

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.tdscdma_nmr_obj.serialize_json(item))
    return out


def deserialize_json(data: list) -> TdscdmaNmrList:
    import aws_sdk_iot_wireless.types.tdscdma_nmr_obj

    out: TdscdmaNmrList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.tdscdma_nmr_obj.deserialize_json(item))
    return out
