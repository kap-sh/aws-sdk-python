"""Generated from Smithy shape ``com.amazonaws.signer#SigningPlatforms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signer.types.signing_platform

SigningPlatforms: TypeAlias = list["capo_signer.types.signing_platform.SigningPlatform"]


# --- restJson1 ser/de ---
def serialize_json(value: SigningPlatforms) -> list:
    import capo_signer.types.signing_platform

    out: list = []
    for item in value:
        out.append(capo_signer.types.signing_platform.serialize_json(item))
    return out


def deserialize_json(data: list) -> SigningPlatforms:
    import capo_signer.types.signing_platform

    out: SigningPlatforms = []
    for item in data:
        out.append(capo_signer.types.signing_platform.deserialize_json(item))
    return out
