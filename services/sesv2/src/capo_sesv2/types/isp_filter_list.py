"""Generated from Smithy shape ``com.amazonaws.sesv2#IspFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.isp

IspFilterList: TypeAlias = list["capo_sesv2.types.isp.Isp"]


# --- restJson1 ser/de ---
def serialize_json(value: IspFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> IspFilterList:
    return list(data)
