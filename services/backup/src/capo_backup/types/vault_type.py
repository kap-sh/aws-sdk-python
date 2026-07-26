"""Generated from Smithy shape ``com.amazonaws.backup#VaultType``."""

from typing import Literal, TypeAlias, cast

VaultType: TypeAlias = Literal[
    "BACKUP_VAULT",
    "LOGICALLY_AIR_GAPPED_BACKUP_VAULT",
    "RESTORE_ACCESS_BACKUP_VAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: VaultType) -> str:
    return value


def deserialize_json(data: str) -> VaultType:
    return cast(VaultType, data)
