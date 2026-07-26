"""Generated from Smithy shape ``com.amazonaws.appmesh#PortSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.port_number

PortSet: TypeAlias = list["capo_app_mesh.types.port_number.PortNumber"]


# --- restJson1 ser/de ---
def serialize_json(value: PortSet) -> list:
    return list(value)


def deserialize_json(data: list) -> PortSet:
    return list(data)
