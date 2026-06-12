"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateUsageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

CertificateUsageType: TypeAlias = Literal[
    "SIGNING",
    "ENCRYPTION",
    "TLS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIGNING",
        "ENCRYPTION",
        "TLS",
    )
)


def serialize_aws_json_1_1(value: CertificateUsageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateUsageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateUsageType value: {data!r}")
    return cast(CertificateUsageType, data)
