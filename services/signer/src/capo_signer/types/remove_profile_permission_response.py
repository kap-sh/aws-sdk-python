"""Generated from Smithy shape ``com.amazonaws.signer#RemoveProfilePermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.string


class RemoveProfilePermissionResponse(TypedDict, closed=True):
    revision_id: NotRequired["capo_signer.types.string.String"]
    """<p>An identifier for the current revision of the profile permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveProfilePermissionResponse) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> RemoveProfilePermissionResponse:
    out: RemoveProfilePermissionResponse = {}  # type: ignore[typeddict-item]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    return out
