"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateVirtualRouterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_data


class UpdateVirtualRouterOutput(TypedDict, closed=True):
    virtual_router: "capo_app_mesh.types.virtual_router_data.VirtualRouterData"
    """<p>A full description of the virtual router that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualRouterOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_router_data

    out["virtualRouter"] = capo_app_mesh.types.virtual_router_data.serialize_json(
        value["virtual_router"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVirtualRouterOutput:
    out: UpdateVirtualRouterOutput = {}  # type: ignore[typeddict-item]
    if "virtualRouter" in data:
        import capo_app_mesh.types.virtual_router_data

        out["virtual_router"] = (
            capo_app_mesh.types.virtual_router_data.deserialize_json(
                data["virtualRouter"]
            )
        )
    else:
        raise DeserializationError("UpdateVirtualRouterOutput.virtual_router required")
    return out
