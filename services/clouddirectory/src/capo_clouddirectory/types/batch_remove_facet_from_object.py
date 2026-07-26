"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchRemoveFacetFromObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet


class BatchRemoveFacetFromObject(TypedDict, closed=True):
    schema_facet: "capo_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>The facet to remove from the object.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object whose facet will be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveFacetFromObject) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.schema_facet

    out["SchemaFacet"] = capo_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    return out


def deserialize_json(data: dict) -> BatchRemoveFacetFromObject:
    out: BatchRemoveFacetFromObject = {}  # type: ignore[typeddict-item]
    if "SchemaFacet" in data:
        import capo_clouddirectory.types.schema_facet

        out["schema_facet"] = capo_clouddirectory.types.schema_facet.deserialize_json(
            data["SchemaFacet"]
        )
    else:
        raise DeserializationError("BatchRemoveFacetFromObject.schema_facet required")
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "BatchRemoveFacetFromObject.object_reference required"
        )
    return out
