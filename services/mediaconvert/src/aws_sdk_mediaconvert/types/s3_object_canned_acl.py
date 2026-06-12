"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3ObjectCannedAcl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose an Amazon S3 canned ACL for MediaConvert to apply to this output."""
S3ObjectCannedAcl: TypeAlias = Literal[
    "PUBLIC_READ",
    "AUTHENTICATED_READ",
    "BUCKET_OWNER_READ",
    "BUCKET_OWNER_FULL_CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_READ",
        "AUTHENTICATED_READ",
        "BUCKET_OWNER_READ",
        "BUCKET_OWNER_FULL_CONTROL",
    )
)


def serialize_json(value: S3ObjectCannedAcl) -> str:
    return value


def deserialize_json(data: str) -> S3ObjectCannedAcl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3ObjectCannedAcl value: {data!r}")
    return cast(S3ObjectCannedAcl, data)
