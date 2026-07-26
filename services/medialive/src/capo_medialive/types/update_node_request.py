"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateNodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.node_role
    import capo_medialive.types.sdi_source_mappings_update_request


class UpdateNodeRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster"""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Include this parameter only if you want to change the current name of the Node. Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive."""
    node_id: "capo_medialive.types.__string.__string"
    """The ID of the node."""
    role: NotRequired["capo_medialive.types.node_role.NodeRole"]
    """The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails."""
    sdi_source_mappings: NotRequired[
        "capo_medialive.types.sdi_source_mappings_update_request.SdiSourceMappingsUpdateRequest"
    ]
    """The mappings of a SDI capture card port to a logical SDI data stream"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodeRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "role" in value:
        import capo_medialive.types.node_role

        out["role"] = capo_medialive.types.node_role.serialize_json(value["role"])
    if "sdi_source_mappings" in value:
        import capo_medialive.types.sdi_source_mappings_update_request

        out["sdiSourceMappings"] = (
            capo_medialive.types.sdi_source_mappings_update_request.serialize_json(
                value["sdi_source_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNodeRequest:
    out: UpdateNodeRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "role" in data:
        import capo_medialive.types.node_role

        out["role"] = capo_medialive.types.node_role.deserialize_json(data["role"])
    if "sdiSourceMappings" in data:
        import capo_medialive.types.sdi_source_mappings_update_request

        out["sdi_source_mappings"] = (
            capo_medialive.types.sdi_source_mappings_update_request.deserialize_json(
                data["sdiSourceMappings"]
            )
        )
    return out
