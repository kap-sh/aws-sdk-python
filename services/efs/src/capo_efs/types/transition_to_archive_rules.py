"""Generated from Smithy shape ``com.amazonaws.efs#TransitionToArchiveRules``."""

from typing import Literal, TypeAlias, cast

TransitionToArchiveRules: TypeAlias = Literal[
    "AFTER_1_DAY",
    "AFTER_7_DAYS",
    "AFTER_14_DAYS",
    "AFTER_30_DAYS",
    "AFTER_60_DAYS",
    "AFTER_90_DAYS",
    "AFTER_180_DAYS",
    "AFTER_270_DAYS",
    "AFTER_365_DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitionToArchiveRules) -> str:
    return value


def deserialize_json(data: str) -> TransitionToArchiveRules:
    return cast(TransitionToArchiveRules, data)
