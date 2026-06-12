"""Generated from Smithy shape ``com.amazonaws.acmpca#S3ObjectAcl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

S3ObjectAcl: TypeAlias = Literal[
    "PUBLIC_READ",
    "BUCKET_OWNER_FULL_CONTROL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_READ",
        "BUCKET_OWNER_FULL_CONTROL",
    )
)


def serialize_aws_json_1_1(value: S3ObjectAcl) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3ObjectAcl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3ObjectAcl value: {data!r}")
    return cast(S3ObjectAcl, data)
