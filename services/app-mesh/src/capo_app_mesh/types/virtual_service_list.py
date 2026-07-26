"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_service_ref

VirtualServiceList: TypeAlias = list[
    "capo_app_mesh.types.virtual_service_ref.VirtualServiceRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceList) -> list:
    import capo_app_mesh.types.virtual_service_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.virtual_service_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualServiceList:
    import capo_app_mesh.types.virtual_service_ref

    out: VirtualServiceList = []
    for item in data:
        out.append(capo_app_mesh.types.virtual_service_ref.deserialize_json(item))
    return out
