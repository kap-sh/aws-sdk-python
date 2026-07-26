"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TrailPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.trail_properties

TrailPropertiesList: TypeAlias = list[
    "capo_accessanalyzer.types.trail_properties.TrailProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrailPropertiesList) -> list:
    import capo_accessanalyzer.types.trail_properties

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.trail_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrailPropertiesList:
    import capo_accessanalyzer.types.trail_properties

    out: TrailPropertiesList = []
    for item in data:
        out.append(capo_accessanalyzer.types.trail_properties.deserialize_json(item))
    return out
