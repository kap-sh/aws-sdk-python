"""Generated from Smithy shape ``com.amazonaws.signer#Statuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.signing_profile_status

Statuses: TypeAlias = list[
    "aws_sdk_signer.types.signing_profile_status.SigningProfileStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: Statuses) -> list:
    import aws_sdk_signer.types.signing_profile_status

    out: list = []
    for item in value:
        out.append(aws_sdk_signer.types.signing_profile_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> Statuses:
    import aws_sdk_signer.types.signing_profile_status

    out: Statuses = []
    for item in data:
        out.append(aws_sdk_signer.types.signing_profile_status.deserialize_json(item))
    return out
