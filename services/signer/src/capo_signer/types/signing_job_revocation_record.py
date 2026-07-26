"""Generated from Smithy shape ``com.amazonaws.signer#SigningJobRevocationRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.string
    import capo_signer.types.timestamp


class SigningJobRevocationRecord(TypedDict, closed=True):
    reason: NotRequired["capo_signer.types.string.String"]
    """<p>A caller-supplied reason for revocation.</p>"""
    revoked_at: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>The time of revocation.</p>"""
    revoked_by: NotRequired["capo_signer.types.string.String"]
    """<p>The identity of the revoker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningJobRevocationRecord) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "revoked_at" in value:
        import capo_signer.types.timestamp

        out["revokedAt"] = capo_signer.types.timestamp.serialize_json(
            value["revoked_at"]
        )
    if "revoked_by" in value:
        out["revokedBy"] = value["revoked_by"]
    return out


def deserialize_json(data: dict) -> SigningJobRevocationRecord:
    out: SigningJobRevocationRecord = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "revokedAt" in data:
        import capo_signer.types.timestamp

        out["revoked_at"] = capo_signer.types.timestamp.deserialize_json(
            data["revokedAt"]
        )
    if "revokedBy" in data:
        out["revoked_by"] = data["revokedBy"]
    return out
