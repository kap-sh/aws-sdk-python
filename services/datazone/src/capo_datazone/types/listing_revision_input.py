"""Generated from Smithy shape ``com.amazonaws.datazone#ListingRevisionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class ListingRevisionInput(TypedDict, closed=True):
    identifier: "capo_datazone.types.listing_id.ListingId"
    """<p>An identifier of revision to be made to an asset published in a Amazon DataZone catalog.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The details of a revision to be made to an asset published in a Amazon DataZone catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingRevisionInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ListingRevisionInput:
    out: ListingRevisionInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("ListingRevisionInput.identifier required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("ListingRevisionInput.revision required")
    return out
