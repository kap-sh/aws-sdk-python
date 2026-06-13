"""Generated from Smithy shape ``com.amazonaws.backup#MpaSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

MpaSessionStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "APPROVED",
        "FAILED",
    )
)


def serialize_json(value: MpaSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> MpaSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MpaSessionStatus value: {data!r}")
    return cast(MpaSessionStatus, data)
