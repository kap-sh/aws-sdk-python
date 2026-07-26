"""Generated from Smithy shape ``com.amazonaws.inspector2#DateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.date_filter

DateFilterList: TypeAlias = list["capo_inspector2.types.date_filter.DateFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: DateFilterList) -> list:
    import capo_inspector2.types.date_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.date_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DateFilterList:
    import capo_inspector2.types.date_filter

    out: DateFilterList = []
    for item in data:
        out.append(capo_inspector2.types.date_filter.deserialize_json(item))
    return out
