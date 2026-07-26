"""Generated from Smithy shape ``com.amazonaws.sustainability#EmissionsTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.emissions_type

EmissionsTypeList: TypeAlias = list[
    "capo_sustainability.types.emissions_type.EmissionsType"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmissionsTypeList) -> list:
    import capo_sustainability.types.emissions_type

    out: list = []
    for item in value:
        out.append(capo_sustainability.types.emissions_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmissionsTypeList:
    import capo_sustainability.types.emissions_type

    out: EmissionsTypeList = []
    for item in data:
        out.append(capo_sustainability.types.emissions_type.deserialize_json(item))
    return out
