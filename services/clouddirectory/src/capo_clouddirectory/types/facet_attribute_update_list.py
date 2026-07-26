"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.facet_attribute_update

FacetAttributeUpdateList: TypeAlias = list[
    "capo_clouddirectory.types.facet_attribute_update.FacetAttributeUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeUpdateList) -> list:
    import capo_clouddirectory.types.facet_attribute_update

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.facet_attribute_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FacetAttributeUpdateList:
    import capo_clouddirectory.types.facet_attribute_update

    out: FacetAttributeUpdateList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.facet_attribute_update.deserialize_json(item)
        )
    return out
