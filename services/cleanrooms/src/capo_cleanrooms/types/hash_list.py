"""Generated from Smithy shape ``com.amazonaws.cleanrooms#HashList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.hash

HashList: TypeAlias = list["capo_cleanrooms.types.hash.Hash"]


# --- restJson1 ser/de ---
def serialize_json(value: HashList) -> list:
    import capo_cleanrooms.types.hash

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.hash.serialize_json(item))
    return out


def deserialize_json(data: list) -> HashList:
    import capo_cleanrooms.types.hash

    out: HashList = []
    for item in data:
        out.append(capo_cleanrooms.types.hash.deserialize_json(item))
    return out
