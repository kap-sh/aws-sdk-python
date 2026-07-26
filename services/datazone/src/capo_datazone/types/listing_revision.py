"""Generated from Smithy shape ``com.amazonaws.datazone#ListingRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class ListingRevision(TypedDict, closed=True):
    id: "capo_datazone.types.listing_id.ListingId"
    """<p>An identifier of a revision of an asset published in a Amazon DataZone catalog.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The details of a revision of an asset published in a Amazon DataZone catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingRevision) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ListingRevision:
    out: ListingRevision = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListingRevision.id required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("ListingRevision.revision required")
    return out
