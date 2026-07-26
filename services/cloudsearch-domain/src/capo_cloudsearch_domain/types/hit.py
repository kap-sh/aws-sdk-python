"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Hit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.exprs
    import capo_cloudsearch_domain.types.fields
    import capo_cloudsearch_domain.types.highlights
    import capo_cloudsearch_domain.types.string


class Hit(TypedDict, closed=True):
    id: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The document ID of a document that matches the search request.</p>"""
    fields: NotRequired["capo_cloudsearch_domain.types.fields.Fields"]
    """<p>The fields returned from a document that matches the search request.</p>"""
    exprs: NotRequired["capo_cloudsearch_domain.types.exprs.Exprs"]
    """<p>The expressions returned from a document that matches the search request.</p>"""
    highlights: NotRequired["capo_cloudsearch_domain.types.highlights.Highlights"]
    """<p>The highlights returned from a document that matches the search request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Hit) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "fields" in value:
        import capo_cloudsearch_domain.types.fields

        out["fields"] = capo_cloudsearch_domain.types.fields.serialize_json(
            value["fields"]
        )
    if "exprs" in value:
        import capo_cloudsearch_domain.types.exprs

        out["exprs"] = capo_cloudsearch_domain.types.exprs.serialize_json(
            value["exprs"]
        )
    if "highlights" in value:
        import capo_cloudsearch_domain.types.highlights

        out["highlights"] = capo_cloudsearch_domain.types.highlights.serialize_json(
            value["highlights"]
        )
    return out


def deserialize_json(data: dict) -> Hit:
    out: Hit = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "fields" in data:
        import capo_cloudsearch_domain.types.fields

        out["fields"] = capo_cloudsearch_domain.types.fields.deserialize_json(
            data["fields"]
        )
    if "exprs" in data:
        import capo_cloudsearch_domain.types.exprs

        out["exprs"] = capo_cloudsearch_domain.types.exprs.deserialize_json(
            data["exprs"]
        )
    if "highlights" in data:
        import capo_cloudsearch_domain.types.highlights

        out["highlights"] = capo_cloudsearch_domain.types.highlights.deserialize_json(
            data["highlights"]
        )
    return out
