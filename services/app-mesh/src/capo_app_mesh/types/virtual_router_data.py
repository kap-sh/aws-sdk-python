"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.resource_metadata
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.virtual_router_spec
    import capo_app_mesh.types.virtual_router_status


class VirtualRouterData(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual router resides in.</p>"""
    virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual router.</p>"""
    spec: "capo_app_mesh.types.virtual_router_spec.VirtualRouterSpec"
    """<p>The specifications of the virtual router.</p>"""
    metadata: "capo_app_mesh.types.resource_metadata.ResourceMetadata"
    """<p>The associated metadata for the virtual router.</p>"""
    status: "capo_app_mesh.types.virtual_router_status.VirtualRouterStatus"
    """<p>The current status of the virtual router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualRouterName"] = value["virtual_router_name"]
    import capo_app_mesh.types.virtual_router_spec

    out["spec"] = capo_app_mesh.types.virtual_router_spec.serialize_json(value["spec"])
    import capo_app_mesh.types.resource_metadata

    out["metadata"] = capo_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import capo_app_mesh.types.virtual_router_status

    out["status"] = capo_app_mesh.types.virtual_router_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VirtualRouterData:
    out: VirtualRouterData = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("VirtualRouterData.mesh_name required")
    if "virtualRouterName" in data:
        out["virtual_router_name"] = data["virtualRouterName"]
    else:
        raise DeserializationError("VirtualRouterData.virtual_router_name required")
    if "spec" in data:
        import capo_app_mesh.types.virtual_router_spec

        out["spec"] = capo_app_mesh.types.virtual_router_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("VirtualRouterData.spec required")
    if "metadata" in data:
        import capo_app_mesh.types.resource_metadata

        out["metadata"] = capo_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("VirtualRouterData.metadata required")
    if "status" in data:
        import capo_app_mesh.types.virtual_router_status

        out["status"] = capo_app_mesh.types.virtual_router_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("VirtualRouterData.status required")
    return out
