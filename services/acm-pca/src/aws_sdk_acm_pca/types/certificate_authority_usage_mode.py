"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityUsageMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

CertificateAuthorityUsageMode: TypeAlias = Literal[
    "GENERAL_PURPOSE",
    "SHORT_LIVED_CERTIFICATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERAL_PURPOSE",
        "SHORT_LIVED_CERTIFICATE",
    )
)


def serialize_aws_json_1_1(value: CertificateAuthorityUsageMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateAuthorityUsageMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateAuthorityUsageMode value: {data!r}"
        )
    return cast(CertificateAuthorityUsageMode, data)
