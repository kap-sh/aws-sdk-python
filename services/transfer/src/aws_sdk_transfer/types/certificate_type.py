"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

CertificateType: TypeAlias = Literal[
    "CERTIFICATE",
    "CERTIFICATE_WITH_PRIVATE_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CERTIFICATE",
        "CERTIFICATE_WITH_PRIVATE_KEY",
    )
)


def serialize_aws_json_1_1(value: CertificateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateType value: {data!r}")
    return cast(CertificateType, data)
