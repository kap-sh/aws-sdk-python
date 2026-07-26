"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateVirtualNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_node_data


class UpdateVirtualNodeOutput(TypedDict, closed=True):
    virtual_node: "capo_app_mesh.types.virtual_node_data.VirtualNodeData"
    """<p>A full description of the virtual node that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualNodeOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_node_data

    out["virtualNode"] = capo_app_mesh.types.virtual_node_data.serialize_json(
        value["virtual_node"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVirtualNodeOutput:
    out: UpdateVirtualNodeOutput = {}  # type: ignore[typeddict-item]
    if "virtualNode" in data:
        import capo_app_mesh.types.virtual_node_data

        out["virtual_node"] = capo_app_mesh.types.virtual_node_data.deserialize_json(
            data["virtualNode"]
        )
    else:
        raise DeserializationError("UpdateVirtualNodeOutput.virtual_node required")
    return out
