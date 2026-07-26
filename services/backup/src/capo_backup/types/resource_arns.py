"""Generated from Smithy shape ``com.amazonaws.backup#ResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.arn

ResourceArns: TypeAlias = list["capo_backup.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArns:
    return list(data)
