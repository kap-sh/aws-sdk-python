"""Generated from Smithy shape ``com.amazonaws.securityir#CaseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

CaseStatus: TypeAlias = Literal[
    "Submitted",
    "Acknowledged",
    "Detection and Analysis",
    "Containment, Eradication and Recovery",
    "Post-incident Activities",
    "Ready to Close",
    "Closed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Submitted",
        "Acknowledged",
        "Detection and Analysis",
        "Containment, Eradication and Recovery",
        "Post-incident Activities",
        "Ready to Close",
        "Closed",
    )
)


def serialize_json(value: CaseStatus) -> str:
    return value


def deserialize_json(data: str) -> CaseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CaseStatus value: {data!r}")
    return cast(CaseStatus, data)
