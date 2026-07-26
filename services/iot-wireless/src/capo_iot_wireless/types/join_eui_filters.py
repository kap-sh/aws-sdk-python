"""Generated from Smithy shape ``com.amazonaws.iotwireless#JoinEuiFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.join_eui_range

JoinEuiFilters: TypeAlias = list["capo_iot_wireless.types.join_eui_range.JoinEuiRange"]


# --- restJson1 ser/de ---
def serialize_json(value: JoinEuiFilters) -> list:
    import capo_iot_wireless.types.join_eui_range

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.join_eui_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> JoinEuiFilters:
    import capo_iot_wireless.types.join_eui_range

    out: JoinEuiFilters = []
    for item in data:
        out.append(capo_iot_wireless.types.join_eui_range.deserialize_json(item))
    return out
