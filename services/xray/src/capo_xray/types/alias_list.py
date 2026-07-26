"""Generated from Smithy shape ``com.amazonaws.xray#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.alias

AliasList: TypeAlias = list["capo_xray.types.alias.Alias"]


# --- restJson1 ser/de ---
def serialize_json(value: AliasList) -> list:
    import capo_xray.types.alias

    out: list = []
    for item in value:
        out.append(capo_xray.types.alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> AliasList:
    import capo_xray.types.alias

    out: AliasList = []
    for item in data:
        out.append(capo_xray.types.alias.deserialize_json(item))
    return out
