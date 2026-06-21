"""Generated from Smithy shape ``com.amazonaws.securityhub#VerificationState``."""

from typing import Literal, TypeAlias, cast

VerificationState: TypeAlias = Literal[
    "UNKNOWN",
    "TRUE_POSITIVE",
    "FALSE_POSITIVE",
    "BENIGN_POSITIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationState) -> str:
    return value


def deserialize_json(data: str) -> VerificationState:
    return cast(VerificationState, data)
