"""Generated from Smithy shape ``com.amazonaws.backup#ResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.resource_type

ResourceTypes: TypeAlias = list["aws_sdk_backup.types.resource_type.ResourceType"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypes:
    return list(data)
