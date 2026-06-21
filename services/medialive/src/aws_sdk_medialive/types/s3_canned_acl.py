"""Generated from Smithy shape ``com.amazonaws.medialive#S3CannedAcl``."""

from typing import Literal, TypeAlias, cast

"""S3 Canned Acl"""
S3CannedAcl: TypeAlias = Literal[
    "AUTHENTICATED_READ",
    "BUCKET_OWNER_FULL_CONTROL",
    "BUCKET_OWNER_READ",
    "PUBLIC_READ",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3CannedAcl) -> str:
    return value


def deserialize_json(data: str) -> S3CannedAcl:
    return cast(S3CannedAcl, data)
