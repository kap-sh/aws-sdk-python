"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet


class ListObjectAttributesRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object whose attributes will be listed.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>"""
    facet_filter: NotRequired["capo_clouddirectory.types.schema_facet.SchemaFacet"]
    """<p>Used to filter the list of object attributes that are associated with a certain facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectAttributesRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "facet_filter" in value:
        import capo_clouddirectory.types.schema_facet

        out["FacetFilter"] = capo_clouddirectory.types.schema_facet.serialize_json(
            value["facet_filter"]
        )
    return out


def deserialize_json(data: dict) -> ListObjectAttributesRequest:
    out: ListObjectAttributesRequest = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "ListObjectAttributesRequest.object_reference required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "FacetFilter" in data:
        import capo_clouddirectory.types.schema_facet

        out["facet_filter"] = capo_clouddirectory.types.schema_facet.deserialize_json(
            data["FacetFilter"]
        )
    return out
