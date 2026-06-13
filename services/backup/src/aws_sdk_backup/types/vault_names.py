"""Generated from Smithy shape ``com.amazonaws.backup#VaultNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.string

VaultNames: TypeAlias = list["aws_sdk_backup.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: VaultNames) -> list:
    return list(value)


def deserialize_json(data: list) -> VaultNames:
    return list(data)
