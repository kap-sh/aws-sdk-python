"""Generated from Smithy shape ``com.amazonaws.securityir#CaseAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

CaseAttachmentStatus: TypeAlias = Literal[
    "Verified",
    "Failed",
    "Pending",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Verified",
        "Failed",
        "Pending",
    )
)


def serialize_json(value: CaseAttachmentStatus) -> str:
    return value


def deserialize_json(data: str) -> CaseAttachmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CaseAttachmentStatus value: {data!r}")
    return cast(CaseAttachmentStatus, data)
