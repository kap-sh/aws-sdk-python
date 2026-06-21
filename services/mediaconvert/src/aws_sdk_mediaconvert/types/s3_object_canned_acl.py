"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3ObjectCannedAcl``."""

from typing import Literal, TypeAlias, cast

"""Choose an Amazon S3 canned ACL for MediaConvert to apply to this output."""
S3ObjectCannedAcl: TypeAlias = Literal[
    "PUBLIC_READ",
    "AUTHENTICATED_READ",
    "BUCKET_OWNER_READ",
    "BUCKET_OWNER_FULL_CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectCannedAcl) -> str:
    return value


def deserialize_json(data: str) -> S3ObjectCannedAcl:
    return cast(S3ObjectCannedAcl, data)
