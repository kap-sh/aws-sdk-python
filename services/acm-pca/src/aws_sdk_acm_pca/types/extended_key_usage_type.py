"""Generated from Smithy shape ``com.amazonaws.acmpca#ExtendedKeyUsageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

ExtendedKeyUsageType: TypeAlias = Literal[
    "SERVER_AUTH",
    "CLIENT_AUTH",
    "CODE_SIGNING",
    "EMAIL_PROTECTION",
    "TIME_STAMPING",
    "OCSP_SIGNING",
    "SMART_CARD_LOGIN",
    "DOCUMENT_SIGNING",
    "CERTIFICATE_TRANSPARENCY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVER_AUTH",
        "CLIENT_AUTH",
        "CODE_SIGNING",
        "EMAIL_PROTECTION",
        "TIME_STAMPING",
        "OCSP_SIGNING",
        "SMART_CARD_LOGIN",
        "DOCUMENT_SIGNING",
        "CERTIFICATE_TRANSPARENCY",
    )
)


def serialize_aws_json_1_1(value: ExtendedKeyUsageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExtendedKeyUsageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExtendedKeyUsageType value: {data!r}")
    return cast(ExtendedKeyUsageType, data)
