"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.connection

ConnectionList: TypeAlias = list["capo_networkmanager.types.connection.Connection"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionList) -> list:
    import capo_networkmanager.types.connection

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectionList:
    import capo_networkmanager.types.connection

    out: ConnectionList = []
    for item in data:
        out.append(capo_networkmanager.types.connection.deserialize_json(item))
    return out
