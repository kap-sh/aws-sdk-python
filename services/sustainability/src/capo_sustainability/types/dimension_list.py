"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.dimension

DimensionList: TypeAlias = list["capo_sustainability.types.dimension.Dimension"]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionList) -> list:
    import capo_sustainability.types.dimension

    out: list = []
    for item in value:
        out.append(capo_sustainability.types.dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionList:
    import capo_sustainability.types.dimension

    out: DimensionList = []
    for item in data:
        out.append(capo_sustainability.types.dimension.deserialize_json(item))
    return out
