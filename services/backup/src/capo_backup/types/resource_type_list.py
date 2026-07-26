"""Generated from Smithy shape ``com.amazonaws.backup#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.arn

ResourceTypeList: TypeAlias = list["capo_backup.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypeList:
    return list(data)
