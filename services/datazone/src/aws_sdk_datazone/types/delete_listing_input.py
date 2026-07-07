"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteListingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.listing_id


class DeleteListingInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    identifier: "aws_sdk_datazone.types.listing_id.ListingId"
    """<p>The ID of the listing to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteListingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteListingInput:
    out: DeleteListingInput = {}  # type: ignore[typeddict-item]
    return out
