"""Generated from Smithy shape ``com.amazonaws.iotsitewise#IDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.id

IDs: TypeAlias = list["capo_iotsitewise.types.id.ID"]


# --- restJson1 ser/de ---
def serialize_json(value: IDs) -> list:
    return list(value)


def deserialize_json(data: list) -> IDs:
    return list(data)
