"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

CertificateAuthorityStatus: TypeAlias = Literal[
    "CREATING",
    "PENDING_CERTIFICATE",
    "ACTIVE",
    "DELETED",
    "DISABLED",
    "EXPIRED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "PENDING_CERTIFICATE",
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "EXPIRED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CertificateAuthorityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateAuthorityStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateAuthorityStatus value: {data!r}"
        )
    return cast(CertificateAuthorityStatus, data)
