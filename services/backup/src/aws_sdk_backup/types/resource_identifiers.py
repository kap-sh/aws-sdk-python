"""Generated from Smithy shape ``com.amazonaws.backup#ResourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.string

ResourceIdentifiers: TypeAlias = list["aws_sdk_backup.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceIdentifiers:
    return list(data)
