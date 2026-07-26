"""Generated from Smithy shape ``com.amazonaws.signer#SigningProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signer.types.signing_profile

SigningProfiles: TypeAlias = list["capo_signer.types.signing_profile.SigningProfile"]


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfiles) -> list:
    import capo_signer.types.signing_profile

    out: list = []
    for item in value:
        out.append(capo_signer.types.signing_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> SigningProfiles:
    import capo_signer.types.signing_profile

    out: SigningProfiles = []
    for item in data:
        out.append(capo_signer.types.signing_profile.deserialize_json(item))
    return out
