"""Generated from Smithy shape ``com.amazonaws.backup#MpaRevokeSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

MpaRevokeSessionStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FAILED",
    )
)


def serialize_json(value: MpaRevokeSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> MpaRevokeSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MpaRevokeSessionStatus value: {data!r}")
    return cast(MpaRevokeSessionStatus, data)
