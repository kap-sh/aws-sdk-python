"""Generated from Smithy shape ``com.amazonaws.appmesh#Listeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.listener

Listeners: TypeAlias = list["capo_app_mesh.types.listener.Listener"]


# --- restJson1 ser/de ---
def serialize_json(value: Listeners) -> list:
    import capo_app_mesh.types.listener

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.listener.serialize_json(item))
    return out


def deserialize_json(data: list) -> Listeners:
    import capo_app_mesh.types.listener

    out: Listeners = []
    for item in data:
        out.append(capo_app_mesh.types.listener.deserialize_json(item))
    return out
