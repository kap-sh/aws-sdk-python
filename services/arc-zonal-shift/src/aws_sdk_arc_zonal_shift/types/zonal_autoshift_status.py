"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalAutoshiftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

ZonalAutoshiftStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ZonalAutoshiftStatus) -> str:
    return value


def deserialize_json(data: str) -> ZonalAutoshiftStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ZonalAutoshiftStatus value: {data!r}")
    return cast(ZonalAutoshiftStatus, data)
