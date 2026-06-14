"""Generated from Smithy shape ``com.amazonaws.storagegateway#ObjectACL``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

"""<p>A value that sets the access control list (ACL) permission for objects in the S3 bucket that an S3 File Gateway puts objects into. The default value is <code>private</code>.</p>"""
ObjectACL: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
    "aws-exec-read",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "private",
        "public-read",
        "public-read-write",
        "authenticated-read",
        "bucket-owner-read",
        "bucket-owner-full-control",
        "aws-exec-read",
    )
)


def serialize_aws_json_1_1(value: ObjectACL) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectACL:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectACL value: {data!r}")
    return cast(ObjectACL, data)
