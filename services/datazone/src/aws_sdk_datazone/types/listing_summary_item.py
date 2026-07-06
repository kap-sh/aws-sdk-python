"""Generated from Smithy shape ``com.amazonaws.datazone#ListingSummaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.detailed_glossary_terms
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.revision


class ListingSummaryItem(TypedDict, closed=True):
    listing_id: NotRequired["aws_sdk_datazone.types.listing_id.ListingId"]
    """<p>The ID of the data product listing.</p>"""
    listing_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "aws_sdk_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaryItem) -> dict:
    out: dict = {}
    if "listing_id" in value:
        out["listingId"] = value["listing_id"]
    if "listing_revision" in value:
        out["listingRevision"] = value["listing_revision"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListingSummaryItem:
    out: ListingSummaryItem = {}  # type: ignore[typeddict-item]
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    if "listingRevision" in data:
        out["listing_revision"] = data["listingRevision"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    return out
