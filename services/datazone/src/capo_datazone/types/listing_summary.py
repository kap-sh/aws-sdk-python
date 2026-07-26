"""Generated from Smithy shape ``com.amazonaws.datazone#ListingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class ListingSummary(TypedDict, closed=True):
    listing_id: NotRequired["capo_datazone.types.listing_id.ListingId"]
    """<p>The ID of the data product listing.</p>"""
    listing_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummary) -> dict:
    out: dict = {}
    if "listing_id" in value:
        out["listingId"] = value["listing_id"]
    if "listing_revision" in value:
        out["listingRevision"] = value["listing_revision"]
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListingSummary:
    out: ListingSummary = {}  # type: ignore[typeddict-item]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    if "listingRevision" in data:
        out["listing_revision"] = data["listingRevision"]
    if "glossaryTerms" in data:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    return out
