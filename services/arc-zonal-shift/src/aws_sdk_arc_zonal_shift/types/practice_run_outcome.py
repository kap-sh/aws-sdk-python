"""Generated from Smithy shape ``com.amazonaws.arczonalshift#PracticeRunOutcome``."""

from typing import Literal, TypeAlias, cast

PracticeRunOutcome: TypeAlias = Literal[
    "FAILED",
    "INTERRUPTED",
    "PENDING",
    "SUCCEEDED",
    "CAPACITY_CHECK_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PracticeRunOutcome) -> str:
    return value


def deserialize_json(data: str) -> PracticeRunOutcome:
    return cast(PracticeRunOutcome, data)
