"""Generated from Smithy shape ``com.amazonaws.lakeformation#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

VerificationStatus: TypeAlias = Literal[
    "VERIFIED",
    "VERIFICATION_FAILED",
    "NOT_VERIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationStatus) -> str:
    return value


def deserialize_json(data: str) -> VerificationStatus:
    return cast(VerificationStatus, data)
