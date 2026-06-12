"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AppliedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

AppliedStatus: TypeAlias = Literal[
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


def serialize_json(value: AppliedStatus) -> str:
    return value


def deserialize_json(data: str) -> AppliedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppliedStatus value: {data!r}")
    return cast(AppliedStatus, data)
