"""Generated from Smithy shape ``com.amazonaws.greengrassv2#connectivityInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.connectivity_info

connectivityInfoList: TypeAlias = list[
    "capo_greengrassv2.types.connectivity_info.ConnectivityInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: connectivityInfoList) -> list:
    import capo_greengrassv2.types.connectivity_info

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.connectivity_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> connectivityInfoList:
    import capo_greengrassv2.types.connectivity_info

    out: connectivityInfoList = []
    for item in data:
        out.append(capo_greengrassv2.types.connectivity_info.deserialize_json(item))
    return out
