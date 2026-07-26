"""Generated from Smithy shape ``com.amazonaws.clouddirectory#SchemaFacetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.schema_facet

SchemaFacetList: TypeAlias = list["capo_clouddirectory.types.schema_facet.SchemaFacet"]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaFacetList) -> list:
    import capo_clouddirectory.types.schema_facet

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.schema_facet.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaFacetList:
    import capo_clouddirectory.types.schema_facet

    out: SchemaFacetList = []
    for item in data:
        out.append(capo_clouddirectory.types.schema_facet.deserialize_json(item))
    return out
