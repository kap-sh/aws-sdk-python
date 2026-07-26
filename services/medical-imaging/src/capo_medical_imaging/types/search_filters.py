"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.search_filter

SearchFilters: TypeAlias = list["capo_medical_imaging.types.search_filter.SearchFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilters) -> list:
    import capo_medical_imaging.types.search_filter

    out: list = []
    for item in value:
        out.append(capo_medical_imaging.types.search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchFilters:
    import capo_medical_imaging.types.search_filter

    out: SearchFilters = []
    for item in data:
        out.append(capo_medical_imaging.types.search_filter.deserialize_json(item))
    return out
