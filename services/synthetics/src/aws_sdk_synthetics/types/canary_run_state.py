"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunState``."""

from typing import Literal, TypeAlias, cast

CanaryRunState: TypeAlias = Literal[
    "RUNNING",
    "PASSED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunState) -> str:
    return value


def deserialize_json(data: str) -> CanaryRunState:
    return cast(CanaryRunState, data)
