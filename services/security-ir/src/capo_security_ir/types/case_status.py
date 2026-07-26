"""Generated from Smithy shape ``com.amazonaws.securityir#CaseStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CaseStatus) -> str:
    return value


def deserialize_json(data: str) -> CaseStatus:
    return cast(CaseStatus, data)
