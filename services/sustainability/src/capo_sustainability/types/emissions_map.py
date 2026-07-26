"""Generated from Smithy shape ``com.amazonaws.sustainability#EmissionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.emissions
    import capo_sustainability.types.emissions_type

EmissionsMap: TypeAlias = dict[
    "capo_sustainability.types.emissions_type.EmissionsType",
    "capo_sustainability.types.emissions.Emissions",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EmissionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sustainability.types.emissions
        import capo_sustainability.types.emissions_type

        out[capo_sustainability.types.emissions_type.serialize_json(key)] = (
            capo_sustainability.types.emissions.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> EmissionsMap:
    out: EmissionsMap = {}
    for key, value in data.items():
        import capo_sustainability.types.emissions
        import capo_sustainability.types.emissions_type

        out[capo_sustainability.types.emissions_type.deserialize_json(key)] = (
            capo_sustainability.types.emissions.deserialize_json(value)
        )
    return out
