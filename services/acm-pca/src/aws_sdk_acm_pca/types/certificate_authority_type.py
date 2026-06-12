"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

CertificateAuthorityType: TypeAlias = Literal[
    "ROOT",
    "SUBORDINATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROOT",
        "SUBORDINATE",
    )
)


def serialize_aws_json_1_1(value: CertificateAuthorityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateAuthorityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateAuthorityType value: {data!r}")
    return cast(CertificateAuthorityType, data)
