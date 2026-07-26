"""Generated from Smithy shape ``com.amazonaws.signer#SigningProfileRevocationRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.string
    import capo_signer.types.timestamp


class SigningProfileRevocationRecord(TypedDict, closed=True):
    revocation_effective_from: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>The time when revocation becomes effective.</p>"""
    revoked_at: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>The time when the signing profile was revoked.</p>"""
    revoked_by: NotRequired["capo_signer.types.string.String"]
    """<p>The identity of the revoker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfileRevocationRecord) -> dict:
    out: dict = {}
    if "revocation_effective_from" in value:
        import capo_signer.types.timestamp

        out["revocationEffectiveFrom"] = capo_signer.types.timestamp.serialize_json(
            value["revocation_effective_from"]
        )
    if "revoked_at" in value:
        import capo_signer.types.timestamp

        out["revokedAt"] = capo_signer.types.timestamp.serialize_json(
            value["revoked_at"]
        )
    if "revoked_by" in value:
        out["revokedBy"] = value["revoked_by"]
    return out


def deserialize_json(data: dict) -> SigningProfileRevocationRecord:
    out: SigningProfileRevocationRecord = {}  # type: ignore[typeddict-item]
    if "revocationEffectiveFrom" in data:
        import capo_signer.types.timestamp

        out["revocation_effective_from"] = capo_signer.types.timestamp.deserialize_json(
            data["revocationEffectiveFrom"]
        )
    if "revokedAt" in data:
        import capo_signer.types.timestamp

        out["revoked_at"] = capo_signer.types.timestamp.deserialize_json(
            data["revokedAt"]
        )
    if "revokedBy" in data:
        out["revoked_by"] = data["revokedBy"]
    return out
