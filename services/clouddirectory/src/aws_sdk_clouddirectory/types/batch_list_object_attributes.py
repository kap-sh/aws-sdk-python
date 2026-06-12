"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchListObjectAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.schema_facet


class BatchListObjectAttributes(TypedDict):
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference of the object whose attributes need to be listed.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_clouddirectory.types.number_results.NumberResults"
    ]
    """<p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>"""
    facet_filter: NotRequired["aws_sdk_clouddirectory.types.schema_facet.SchemaFacet"]
    """<p>Used to filter the list of object attributes that are associated with a certain facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListObjectAttributes) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "facet_filter" in value:
        import aws_sdk_clouddirectory.types.schema_facet

        out["FacetFilter"] = aws_sdk_clouddirectory.types.schema_facet.serialize_json(
            value["facet_filter"]
        )
    return out


def deserialize_json(data: dict) -> BatchListObjectAttributes:
    out: BatchListObjectAttributes = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "BatchListObjectAttributes.object_reference required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "FacetFilter" in data:
        import aws_sdk_clouddirectory.types.schema_facet

        out["facet_filter"] = (
            aws_sdk_clouddirectory.types.schema_facet.deserialize_json(
                data["FacetFilter"]
            )
        )
    return out
