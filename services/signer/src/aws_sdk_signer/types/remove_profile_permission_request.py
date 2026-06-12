"""Generated from Smithy shape ``com.amazonaws.signer#RemoveProfilePermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.string


class RemoveProfilePermissionRequest(TypedDict):
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>A human-readable name for the signing profile with permissions to be removed.</p>"""
    revision_id: "aws_sdk_signer.types.string.String"
    """<p>An identifier for the current revision of the signing profile permissions.</p>"""
    statement_id: "aws_sdk_signer.types.string.String"
    """<p>A unique identifier for the cross-account permissions statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveProfilePermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveProfilePermissionRequest:
    out: RemoveProfilePermissionRequest = {}  # type: ignore[typeddict-item]
    return out
