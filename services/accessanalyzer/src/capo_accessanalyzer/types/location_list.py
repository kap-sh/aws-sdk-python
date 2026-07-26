"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.location

LocationList: TypeAlias = list["capo_accessanalyzer.types.location.Location"]


# --- restJson1 ser/de ---
def serialize_json(value: LocationList) -> list:
    import capo_accessanalyzer.types.location

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.location.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocationList:
    import capo_accessanalyzer.types.location

    out: LocationList = []
    for item in data:
        out.append(capo_accessanalyzer.types.location.deserialize_json(item))
    return out
