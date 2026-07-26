"""Generated from Smithy shape ``com.amazonaws.appmesh#Backends``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.backend

Backends: TypeAlias = list["capo_app_mesh.types.backend.Backend"]


# --- restJson1 ser/de ---
def serialize_json(value: Backends) -> list:
    import capo_app_mesh.types.backend

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.backend.serialize_json(item))
    return out


def deserialize_json(data: list) -> Backends:
    import capo_app_mesh.types.backend

    out: Backends = []
    for item in data:
        out.append(capo_app_mesh.types.backend.deserialize_json(item))
    return out
