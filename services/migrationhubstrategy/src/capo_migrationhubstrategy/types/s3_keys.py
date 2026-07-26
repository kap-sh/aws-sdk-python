"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#S3Keys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.string

S3Keys: TypeAlias = list["capo_migrationhubstrategy.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: S3Keys) -> list:
    return list(value)


def deserialize_json(data: list) -> S3Keys:
    return list(data)
