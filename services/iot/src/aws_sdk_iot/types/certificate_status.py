"""Generated from Smithy shape ``com.amazonaws.iot#CertificateStatus``."""

from typing import Literal, TypeAlias, cast

CertificateStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "REVOKED",
    "PENDING_TRANSFER",
    "REGISTER_INACTIVE",
    "PENDING_ACTIVATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> CertificateStatus:
    return cast(CertificateStatus, data)
