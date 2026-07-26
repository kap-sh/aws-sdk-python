"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RemoveFacetFromObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet


class RemoveFacetFromObjectRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory in which the object resides.</p>"""
    schema_facet: "capo_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>The facet to remove. See <a>SchemaFacet</a> for details.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object to remove the facet from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFacetFromObjectRequest) -> dict:
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


def deserialize_json(data: dict) -> RemoveFacetFromObjectRequest:
    out: RemoveFacetFromObjectRequest = {}  # type: ignore[typeddict-item]
    if "SchemaFacet" in data:
        import capo_clouddirectory.types.schema_facet

        out["schema_facet"] = capo_clouddirectory.types.schema_facet.deserialize_json(
            data["SchemaFacet"]
        )
    else:
        raise DeserializationError("RemoveFacetFromObjectRequest.schema_facet required")
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveFacetFromObjectRequest.object_reference required"
        )
    return out
