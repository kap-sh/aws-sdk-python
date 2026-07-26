"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TrailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.trail

TrailList: TypeAlias = list["capo_accessanalyzer.types.trail.Trail"]


# --- restJson1 ser/de ---
def serialize_json(value: TrailList) -> list:
    import capo_accessanalyzer.types.trail

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.trail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrailList:
    import capo_accessanalyzer.types.trail

    out: TrailList = []
    for item in data:
        out.append(capo_accessanalyzer.types.trail.deserialize_json(item))
    return out
