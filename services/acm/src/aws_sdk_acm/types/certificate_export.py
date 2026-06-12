"""Generated from Smithy shape ``com.amazonaws.acm#CertificateExport``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

CertificateExport: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: CertificateExport) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateExport:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateExport value: {data!r}")
    return cast(CertificateExport, data)
