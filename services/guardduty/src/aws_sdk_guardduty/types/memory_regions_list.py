"""Generated from Smithy shape ``com.amazonaws.guardduty#MemoryRegionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

MemoryRegionsList: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRegionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> MemoryRegionsList:
    return list(data)
