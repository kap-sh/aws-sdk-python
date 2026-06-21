"""Generated from Smithy shape ``com.amazonaws.securityir#SelfManagedCaseStatus``."""

from typing import Literal, TypeAlias, cast

SelfManagedCaseStatus: TypeAlias = Literal[
    "Submitted",
    "Detection and Analysis",
    "Containment, Eradication and Recovery",
    "Post-incident Activities",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedCaseStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfManagedCaseStatus:
    return cast(SelfManagedCaseStatus, data)
