"""Generated from Smithy shape ``com.amazonaws.acm#CertificateManagedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

CertificateManagedBy: TypeAlias = Literal["CLOUDFRONT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLOUDFRONT",))


def serialize_aws_json_1_1(value: CertificateManagedBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateManagedBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateManagedBy value: {data!r}")
    return cast(CertificateManagedBy, data)
