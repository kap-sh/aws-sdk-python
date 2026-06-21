"""Generated from Smithy shape ``com.amazonaws.sesv2#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

VerificationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "TEMPORARY_FAILURE",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationStatus) -> str:
    return value


def deserialize_json(data: str) -> VerificationStatus:
    return cast(VerificationStatus, data)
