"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Qualities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.quality

Qualities: TypeAlias = list["capo_iotsitewise.types.quality.Quality"]


# --- restJson1 ser/de ---
def serialize_json(value: Qualities) -> list:
    import capo_iotsitewise.types.quality

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.quality.serialize_json(item))
    return out


def deserialize_json(data: list) -> Qualities:
    import capo_iotsitewise.types.quality

    out: Qualities = []
    for item in data:
        out.append(capo_iotsitewise.types.quality.deserialize_json(item))
    return out
