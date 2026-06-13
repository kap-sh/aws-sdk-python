"""Generated from Smithy shape ``com.amazonaws.backup#VaultType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

VaultType: TypeAlias = Literal[
    "BACKUP_VAULT",
    "LOGICALLY_AIR_GAPPED_BACKUP_VAULT",
    "RESTORE_ACCESS_BACKUP_VAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BACKUP_VAULT",
        "LOGICALLY_AIR_GAPPED_BACKUP_VAULT",
        "RESTORE_ACCESS_BACKUP_VAULT",
    )
)


def serialize_json(value: VaultType) -> str:
    return value


def deserialize_json(data: str) -> VaultType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VaultType value: {data!r}")
    return cast(VaultType, data)
