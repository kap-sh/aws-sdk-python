"""Generated from Smithy shape ``com.amazonaws.efs#TransitionToIARules``."""

from typing import Literal, TypeAlias, cast

TransitionToIARules: TypeAlias = Literal[
    "AFTER_7_DAYS",
    "AFTER_14_DAYS",
    "AFTER_30_DAYS",
    "AFTER_60_DAYS",
    "AFTER_90_DAYS",
    "AFTER_1_DAY",
    "AFTER_180_DAYS",
    "AFTER_270_DAYS",
    "AFTER_365_DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitionToIARules) -> str:
    return value


def deserialize_json(data: str) -> TransitionToIARules:
    return cast(TransitionToIARules, data)
