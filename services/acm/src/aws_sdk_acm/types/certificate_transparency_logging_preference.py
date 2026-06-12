"""Generated from Smithy shape ``com.amazonaws.acm#CertificateTransparencyLoggingPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

CertificateTransparencyLoggingPreference: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: CertificateTransparencyLoggingPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateTransparencyLoggingPreference:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateTransparencyLoggingPreference value: {data!r}"
        )
    return cast(CertificateTransparencyLoggingPreference, data)
