"""Generated from Smithy shape ``com.amazonaws.iotwireless#FactoryPresetFreqsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.preset_freq

FactoryPresetFreqsList: TypeAlias = list[
    "capo_iot_wireless.types.preset_freq.PresetFreq"
]


# --- restJson1 ser/de ---
def serialize_json(value: FactoryPresetFreqsList) -> list:
    return list(value)


def deserialize_json(data: list) -> FactoryPresetFreqsList:
    return list(data)
