"""Generated from Smithy shape ``com.amazonaws.signer#RemoveProfilePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.profile_name
    import capo_signer.types.string


class RemoveProfilePermissionRequest(TypedDict, closed=True):
    profile_name: "capo_signer.types.profile_name.ProfileName"
    """<p>A human-readable name for the signing profile with permissions to be removed.</p>"""
    revision_id: "capo_signer.types.string.String"
    """<p>An identifier for the current revision of the signing profile permissions.</p>"""
    statement_id: "capo_signer.types.string.String"
    """<p>A unique identifier for the cross-account permissions statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveProfilePermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveProfilePermissionRequest:
    out: RemoveProfilePermissionRequest = {}  # type: ignore[typeddict-item]
    return out
