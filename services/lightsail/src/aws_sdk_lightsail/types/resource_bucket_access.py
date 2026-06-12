"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceBucketAccess``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ResourceBucketAccess: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "allow",
        "deny",
    )
)


def serialize_aws_json_1_1(value: ResourceBucketAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceBucketAccess:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceBucketAccess value: {data!r}")
    return cast(ResourceBucketAccess, data)
