"""Generated from Smithy shape ``com.amazonaws.efs#TransitionToIARules``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "AFTER_7_DAYS",
        "AFTER_14_DAYS",
        "AFTER_30_DAYS",
        "AFTER_60_DAYS",
        "AFTER_90_DAYS",
        "AFTER_1_DAY",
        "AFTER_180_DAYS",
        "AFTER_270_DAYS",
        "AFTER_365_DAYS",
    )
)


def serialize_json(value: TransitionToIARules) -> str:
    return value


def deserialize_json(data: str) -> TransitionToIARules:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransitionToIARules value: {data!r}")
    return cast(TransitionToIARules, data)
