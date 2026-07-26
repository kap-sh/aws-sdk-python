"""Generated from Smithy shape ``com.amazonaws.iotwireless#JoinEuiRange``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.join_eui

JoinEuiRange: TypeAlias = list["capo_iot_wireless.types.join_eui.JoinEui"]


# --- restJson1 ser/de ---
def serialize_json(value: JoinEuiRange) -> list:
    return list(value)


def deserialize_json(data: list) -> JoinEuiRange:
    return list(data)
