"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftAppliedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

AutoshiftAppliedStatus: TypeAlias = Literal[
    "APPLIED",
    "NOT_APPLIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLIED",
        "NOT_APPLIED",
    )
)


def serialize_json(value: AutoshiftAppliedStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoshiftAppliedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoshiftAppliedStatus value: {data!r}")
    return cast(AutoshiftAppliedStatus, data)
