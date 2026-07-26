"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.facet_name

FacetNameList: TypeAlias = list["capo_clouddirectory.types.facet_name.FacetName"]


# --- restJson1 ser/de ---
def serialize_json(value: FacetNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> FacetNameList:
    return list(data)
