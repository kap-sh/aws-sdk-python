"""Generated from Smithy shape ``com.amazonaws.inspector2#PathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.path

PathList: TypeAlias = list["capo_inspector2.types.path.Path"]


# --- restJson1 ser/de ---
def serialize_json(value: PathList) -> list:
    return list(value)


def deserialize_json(data: list) -> PathList:
    return list(data)
