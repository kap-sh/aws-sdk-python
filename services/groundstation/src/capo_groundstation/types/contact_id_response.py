"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid
    import capo_groundstation.types.version_id


class ContactIdResponse(TypedDict, closed=True):
    contact_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a contact.</p>"""
    version_id: NotRequired["capo_groundstation.types.version_id.VersionId"]
    """<p>Version ID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactIdResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["contactId"] = value["contact_id"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> ContactIdResponse:
    out: ContactIdResponse = {}  # type: ignore[typeddict-item]
    if "contactId" in data:
        out["contact_id"] = data["contactId"]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    return out
