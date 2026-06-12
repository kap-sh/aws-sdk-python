"""Generated from Smithy shape ``com.amazonaws.medialive#S3CannedAcl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""S3 Canned Acl"""
S3CannedAcl: TypeAlias = Literal[
    "AUTHENTICATED_READ",
    "BUCKET_OWNER_FULL_CONTROL",
    "BUCKET_OWNER_READ",
    "PUBLIC_READ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTHENTICATED_READ",
        "BUCKET_OWNER_FULL_CONTROL",
        "BUCKET_OWNER_READ",
        "PUBLIC_READ",
    )
)


def serialize_json(value: S3CannedAcl) -> str:
    return value


def deserialize_json(data: str) -> S3CannedAcl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3CannedAcl value: {data!r}")
    return cast(S3CannedAcl, data)
