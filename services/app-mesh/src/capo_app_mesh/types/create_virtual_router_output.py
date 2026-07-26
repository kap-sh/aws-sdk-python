"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateVirtualRouterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_data


class CreateVirtualRouterOutput(TypedDict, closed=True):
    virtual_router: "capo_app_mesh.types.virtual_router_data.VirtualRouterData"
    """<p>The full description of your virtual router following the create call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualRouterOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_router_data

    out["virtualRouter"] = capo_app_mesh.types.virtual_router_data.serialize_json(
        value["virtual_router"]
    )
    return out


def deserialize_json(data: dict) -> CreateVirtualRouterOutput:
    out: CreateVirtualRouterOutput = {}  # type: ignore[typeddict-item]
    if "virtualRouter" in data:
        import capo_app_mesh.types.virtual_router_data

        out["virtual_router"] = (
            capo_app_mesh.types.virtual_router_data.deserialize_json(
                data["virtualRouter"]
            )
        )
    else:
        raise DeserializationError("CreateVirtualRouterOutput.virtual_router required")
    return out
