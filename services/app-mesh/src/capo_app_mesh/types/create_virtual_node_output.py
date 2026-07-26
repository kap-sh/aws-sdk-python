"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateVirtualNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_node_data


class CreateVirtualNodeOutput(TypedDict, closed=True):
    virtual_node: "capo_app_mesh.types.virtual_node_data.VirtualNodeData"
    """<p>The full description of your virtual node following the create call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualNodeOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_node_data

    out["virtualNode"] = capo_app_mesh.types.virtual_node_data.serialize_json(
        value["virtual_node"]
    )
    return out


def deserialize_json(data: dict) -> CreateVirtualNodeOutput:
    out: CreateVirtualNodeOutput = {}  # type: ignore[typeddict-item]
    if "virtualNode" in data:
        import capo_app_mesh.types.virtual_node_data

        out["virtual_node"] = capo_app_mesh.types.virtual_node_data.deserialize_json(
            data["virtualNode"]
        )
    else:
        raise DeserializationError("CreateVirtualNodeOutput.virtual_node required")
    return out
