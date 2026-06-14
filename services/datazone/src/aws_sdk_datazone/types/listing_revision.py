"""Generated from Smithy shape ``com.amazonaws.datazone#ListingRevision``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.revision


class ListingRevision(TypedDict):
    id: "aws_sdk_datazone.types.listing_id.ListingId"
    """<p>An identifier of a revision of an asset published in a Amazon DataZone catalog.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
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
