"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

CertificateStatusType: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_ROTATION",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING_ROTATION",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: CertificateStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateStatusType value: {data!r}")
    return cast(CertificateStatusType, data)
