"""Generated from Smithy shape ``com.amazonaws.medialive#CreateNodeRegistrationScriptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_node_interface_mapping
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.node_role


class CreateNodeRegistrationScriptRequest(TypedDict, closed=True):
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster"""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """If you're generating a re-registration script for an already existing node, this is where you provide the id."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specify a pattern for MediaLive Anywhere to use to assign a name to each Node in the Cluster. The pattern can include the variables $hn (hostname of the node hardware) and $ts for the date and time that the Node is created, in UTC (for example, 2024-08-20T23:35:12Z)."""
    node_interface_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_node_interface_mapping.__listOfNodeInterfaceMapping"
    ]
    """Documentation update needed"""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources."""
    role: NotRequired["aws_sdk_medialive.types.node_role.NodeRole"]
    """The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeRegistrationScriptRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "node_interface_mappings" in value:
        import aws_sdk_medialive.types.__list_of_node_interface_mapping

        out["nodeInterfaceMappings"] = (
            aws_sdk_medialive.types.__list_of_node_interface_mapping.serialize_json(
                value["node_interface_mappings"]
            )
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "role" in value:
        import aws_sdk_medialive.types.node_role

        out["role"] = aws_sdk_medialive.types.node_role.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> CreateNodeRegistrationScriptRequest:
    out: CreateNodeRegistrationScriptRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "nodeInterfaceMappings" in data:
        import aws_sdk_medialive.types.__list_of_node_interface_mapping

        out["node_interface_mappings"] = (
            aws_sdk_medialive.types.__list_of_node_interface_mapping.deserialize_json(
                data["nodeInterfaceMappings"]
            )
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "role" in data:
        import aws_sdk_medialive.types.node_role

        out["role"] = aws_sdk_medialive.types.node_role.deserialize_json(data["role"])
    return out
