"""Generated from Smithy shape ``com.amazonaws.auditmanager#ShareRequestStatus``."""

from typing import Literal, TypeAlias, cast

ShareRequestStatus: TypeAlias = Literal[
    "ACTIVE",
    "REPLICATING",
    "SHARED",
    "EXPIRING",
    "FAILED",
    "EXPIRED",
    "DECLINED",
    "REVOKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareRequestStatus:
    return cast(ShareRequestStatus, data)
