"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkFacetAttributeUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_link_facet_attribute_update

TypedLinkFacetAttributeUpdateList: TypeAlias = list[
    "capo_clouddirectory.types.typed_link_facet_attribute_update.TypedLinkFacetAttributeUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkFacetAttributeUpdateList) -> list:
    import capo_clouddirectory.types.typed_link_facet_attribute_update

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.typed_link_facet_attribute_update.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TypedLinkFacetAttributeUpdateList:
    import capo_clouddirectory.types.typed_link_facet_attribute_update

    out: TypedLinkFacetAttributeUpdateList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.typed_link_facet_attribute_update.deserialize_json(
                item
            )
        )
    return out
