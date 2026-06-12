"""Generated from Smithy shape ``com.amazonaws.acm#ExtendedKeyUsageName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

ExtendedKeyUsageName: TypeAlias = Literal[
    "TLS_WEB_SERVER_AUTHENTICATION",
    "TLS_WEB_CLIENT_AUTHENTICATION",
    "CODE_SIGNING",
    "EMAIL_PROTECTION",
    "TIME_STAMPING",
    "OCSP_SIGNING",
    "IPSEC_END_SYSTEM",
    "IPSEC_TUNNEL",
    "IPSEC_USER",
    "ANY",
    "NONE",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS_WEB_SERVER_AUTHENTICATION",
        "TLS_WEB_CLIENT_AUTHENTICATION",
        "CODE_SIGNING",
        "EMAIL_PROTECTION",
        "TIME_STAMPING",
        "OCSP_SIGNING",
        "IPSEC_END_SYSTEM",
        "IPSEC_TUNNEL",
        "IPSEC_USER",
        "ANY",
        "NONE",
        "CUSTOM",
    )
)


def serialize_aws_json_1_1(value: ExtendedKeyUsageName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExtendedKeyUsageName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExtendedKeyUsageName value: {data!r}")
    return cast(ExtendedKeyUsageName, data)
