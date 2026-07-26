"""Generated from Smithy shape ``com.amazonaws.iotwireless#SubBands``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.sub_band

SubBands: TypeAlias = list["capo_iot_wireless.types.sub_band.SubBand"]


# --- restJson1 ser/de ---
def serialize_json(value: SubBands) -> list:
    return list(value)


def deserialize_json(data: list) -> SubBands:
    return list(data)
