"""Generated from Smithy shape ``com.amazonaws.signer#SigningProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.signing_profile

SigningProfiles: TypeAlias = list["aws_sdk_signer.types.signing_profile.SigningProfile"]


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfiles) -> list:
    import aws_sdk_signer.types.signing_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_signer.types.signing_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> SigningProfiles:
    import aws_sdk_signer.types.signing_profile

    out: SigningProfiles = []
    for item in data:
        out.append(aws_sdk_signer.types.signing_profile.deserialize_json(item))
    return out
