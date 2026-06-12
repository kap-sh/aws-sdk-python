"""Generated from Smithy shape ``com.amazonaws.medialive#CreateNodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.node_role
    import aws_sdk_medialive.types.tags


class CreateNodeRequest(TypedDict):
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The user-specified name of the Node to be created."""
    node_interface_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request.__listOfNodeInterfaceMappingCreateRequest"
    ]
    """Documentation update needed"""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources."""
    role: NotRequired["aws_sdk_medialive.types.node_role.NodeRole"]
    """The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "node_interface_mappings" in value:
        import aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request

        out["nodeInterfaceMappings"] = (
            aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request.serialize_json(
                value["node_interface_mappings"]
            )
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "role" in value:
        import aws_sdk_medialive.types.node_role

        out["role"] = aws_sdk_medialive.types.node_role.serialize_json(value["role"])
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateNodeRequest:
    out: CreateNodeRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nodeInterfaceMappings" in data:
        import aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request

        out["node_interface_mappings"] = (
            aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request.deserialize_json(
                data["nodeInterfaceMappings"]
            )
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "role" in data:
        import aws_sdk_medialive.types.node_role

        out["role"] = aws_sdk_medialive.types.node_role.deserialize_json(data["role"])
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    return out
