"""Generated from Smithy shape ``com.amazonaws.datazone#GetListingInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.revision


class GetListingInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    identifier: "aws_sdk_datazone.types.listing_id.ListingId"
    """<p>The ID of the listing.</p>"""
    listing_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetListingInput:
    out: GetListingInput = {}  # type: ignore[typeddict-item]
    return out
