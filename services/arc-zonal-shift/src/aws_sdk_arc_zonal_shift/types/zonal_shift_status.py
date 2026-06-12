"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalShiftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

ZonalShiftStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "EXPIRED",
        "CANCELED",
    )
)


def serialize_json(value: ZonalShiftStatus) -> str:
    return value


def deserialize_json(data: str) -> ZonalShiftStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ZonalShiftStatus value: {data!r}")
    return cast(ZonalShiftStatus, data)
