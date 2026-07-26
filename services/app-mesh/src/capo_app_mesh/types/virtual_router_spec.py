"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_listeners


class VirtualRouterSpec(TypedDict, closed=True):
    listeners: NotRequired[
        "capo_app_mesh.types.virtual_router_listeners.VirtualRouterListeners"
    ]
    """<p>The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterSpec) -> dict:
    out: dict = {}
    if "listeners" in value:
        import capo_app_mesh.types.virtual_router_listeners

        out["listeners"] = capo_app_mesh.types.virtual_router_listeners.serialize_json(
            value["listeners"]
        )
    return out


def deserialize_json(data: dict) -> VirtualRouterSpec:
    out: VirtualRouterSpec = {}  # type: ignore[typeddict-item]
    if "listeners" in data:
        import capo_app_mesh.types.virtual_router_listeners

        out["listeners"] = (
            capo_app_mesh.types.virtual_router_listeners.deserialize_json(
                data["listeners"]
            )
        )
    return out
