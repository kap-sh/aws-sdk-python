"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

AutoshiftExecutionStatus: TypeAlias = Literal[
    "ACTIVE",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "COMPLETED",
    )
)


def serialize_json(value: AutoshiftExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoshiftExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoshiftExecutionStatus value: {data!r}")
    return cast(AutoshiftExecutionStatus, data)
