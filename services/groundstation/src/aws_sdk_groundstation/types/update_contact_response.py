"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateContactResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid
    import aws_sdk_groundstation.types.version_id


class UpdateContactResponse(TypedDict):
    contact_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a contact.</p>"""
    version_id: NotRequired["aws_sdk_groundstation.types.version_id.VersionId"]
    """<p>Version ID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["contactId"] = value["contact_id"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> UpdateContactResponse:
    out: UpdateContactResponse = {}  # type: ignore[typeddict-item]
    if "contactId" in data:
        out["contact_id"] = data["contactId"]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    return out
