"""Generated from Smithy shape ``com.amazonaws.athena#S3AclOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

S3AclOption: TypeAlias = Literal["BUCKET_OWNER_FULL_CONTROL",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BUCKET_OWNER_FULL_CONTROL",))


def serialize_aws_json_1_1(value: S3AclOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AclOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3AclOption value: {data!r}")
    return cast(S3AclOption, data)
