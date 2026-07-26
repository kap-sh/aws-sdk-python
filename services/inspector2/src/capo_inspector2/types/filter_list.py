"""Generated from Smithy shape ``com.amazonaws.inspector2#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.filter

FilterList: TypeAlias = list["capo_inspector2.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import capo_inspector2.types.filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import capo_inspector2.types.filter

    out: FilterList = []
    for item in data:
        out.append(capo_inspector2.types.filter.deserialize_json(item))
    return out
