"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ChannelConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.string

ChannelConfigurationMap: TypeAlias = dict[
    "capo_lex_model_building_service.types.string.String",
    "capo_lex_model_building_service.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChannelConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ChannelConfigurationMap:
    out: ChannelConfigurationMap = {}
    for key, value in data.items():
        out[key] = value
    return out
