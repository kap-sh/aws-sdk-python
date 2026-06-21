"""Generated from Smithy shape ``com.amazonaws.iot#VerificationState``."""

from typing import Literal, TypeAlias, cast

VerificationState: TypeAlias = Literal[
    "FALSE_POSITIVE",
    "BENIGN_POSITIVE",
    "TRUE_POSITIVE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationState) -> str:
    return value


def deserialize_json(data: str) -> VerificationState:
    return cast(VerificationState, data)
