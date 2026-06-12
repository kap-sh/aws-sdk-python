"""Generated from Smithy shape ``com.amazonaws.sesv2#IspNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.isp_name

IspNameList: TypeAlias = list["aws_sdk_sesv2.types.isp_name.IspName"]


# --- restJson1 ser/de ---
def serialize_json(value: IspNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> IspNameList:
    return list(data)
