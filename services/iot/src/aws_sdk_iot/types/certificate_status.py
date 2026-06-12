"""Generated from Smithy shape ``com.amazonaws.iot#CertificateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CertificateStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "REVOKED",
    "PENDING_TRANSFER",
    "REGISTER_INACTIVE",
    "PENDING_ACTIVATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "REVOKED",
        "PENDING_TRANSFER",
        "REGISTER_INACTIVE",
        "PENDING_ACTIVATION",
    )
)


def serialize_json(value: CertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> CertificateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateStatus value: {data!r}")
    return cast(CertificateStatus, data)
