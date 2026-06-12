"""Generated from Smithy shape ``com.amazonaws.appstream#CertificateBasedAuthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

CertificateBasedAuthStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK",
    )
)


def serialize_aws_json_1_1(value: CertificateBasedAuthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateBasedAuthStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateBasedAuthStatus value: {data!r}"
        )
    return cast(CertificateBasedAuthStatus, data)
