"""Generated from Smithy shape ``com.amazonaws.acm#CertificateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

CertificateStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "ISSUED",
    "INACTIVE",
    "EXPIRED",
    "VALIDATION_TIMED_OUT",
    "REVOKED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VALIDATION",
        "ISSUED",
        "INACTIVE",
        "EXPIRED",
        "VALIDATION_TIMED_OUT",
        "REVOKED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CertificateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateStatus value: {data!r}")
    return cast(CertificateStatus, data)
