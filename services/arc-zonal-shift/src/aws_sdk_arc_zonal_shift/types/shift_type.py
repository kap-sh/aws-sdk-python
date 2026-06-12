"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ShiftType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

ShiftType: TypeAlias = Literal[
    "ZONAL_SHIFT",
    "PRACTICE_RUN",
    "FIS_EXPERIMENT",
    "ZONAL_AUTOSHIFT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZONAL_SHIFT",
        "PRACTICE_RUN",
        "FIS_EXPERIMENT",
        "ZONAL_AUTOSHIFT",
    )
)


def serialize_json(value: ShiftType) -> str:
    return value


def deserialize_json(data: str) -> ShiftType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShiftType value: {data!r}")
    return cast(ShiftType, data)
