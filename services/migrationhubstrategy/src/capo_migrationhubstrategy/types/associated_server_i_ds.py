"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssociatedServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.string

AssociatedServerIDs: TypeAlias = list["capo_migrationhubstrategy.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociatedServerIDs:
    return list(data)
