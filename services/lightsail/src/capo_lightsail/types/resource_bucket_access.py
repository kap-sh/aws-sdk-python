"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceBucketAccess``."""

from typing import Literal, TypeAlias, cast

ResourceBucketAccess: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceBucketAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceBucketAccess:
    return cast(ResourceBucketAccess, data)
