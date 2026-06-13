"""Generated from Smithy shape ``com.amazonaws.securityir#SelfManagedCaseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

SelfManagedCaseStatus: TypeAlias = Literal[
    "Submitted",
    "Detection and Analysis",
    "Containment, Eradication and Recovery",
    "Post-incident Activities",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Submitted",
        "Detection and Analysis",
        "Containment, Eradication and Recovery",
        "Post-incident Activities",
    )
)


def serialize_json(value: SelfManagedCaseStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfManagedCaseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelfManagedCaseStatus value: {data!r}")
    return cast(SelfManagedCaseStatus, data)
