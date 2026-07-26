"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterListener``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.port_mapping


class VirtualRouterListener(TypedDict, closed=True):
    port_mapping: "capo_app_mesh.types.port_mapping.PortMapping"


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterListener) -> dict:
    out: dict = {}
    import capo_app_mesh.types.port_mapping

    out["portMapping"] = capo_app_mesh.types.port_mapping.serialize_json(
        value["port_mapping"]
    )
    return out


def deserialize_json(data: dict) -> VirtualRouterListener:
    out: VirtualRouterListener = {}  # type: ignore[typeddict-item]
    if "portMapping" in data:
        import capo_app_mesh.types.port_mapping

        out["port_mapping"] = capo_app_mesh.types.port_mapping.deserialize_json(
            data["portMapping"]
        )
    else:
        raise DeserializationError("VirtualRouterListener.port_mapping required")
    return out
